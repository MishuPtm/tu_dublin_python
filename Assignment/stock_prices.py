"""
Author: Ionut Petrescu
Date: 16.11.2019
Assignment DT249 PA1

our program should calculate the monthly and yearly average price for Google
and tell us the best and worst six months and the best and worst six years for Google.
"""
import csv
import requests
import datetime as dt
company_name = ""


def make_nb_if_nb(str_input):
    try:
        number = float(str_input)
        return number if '.' in str_input else int(number)
    except ValueError:
        return str_input


# Gets stock data about a specific company, accepts Symbol string or an array with [Symbol, Name, Category]
def get_stock_from_api(company=None):
    if isinstance(company, str):
        company = [company.upper(), f"{company} - (full name not available)", "Unknown category"]

    global company_name
    company_name = company[1]

    try:
        from timeit import default_timer as timer
        start = timer()
        print(f"Please wait while downloading data for {company[1]}")
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&" \
              f"symbol={company[0]}&outputsize=full&datatype=csv&apikey=AVQVWNZSUJRRKKQJ"
        response = requests.request("GET", url)
        end = timer()
        print(f"Finished downloading in {end - start} seconds")

        if "Error" in response.text:
            print(f"No company found under the name of {company[0]}")
            return None
        return response.text
    except:
        return None


# Returns content from a link
def get_content_from_link(link):
    try:
        response = requests.get(link, timeout=3)
        if response.ok:
            return response.content.decode()
        else:
            raise Exception
    except:
        print(f"Unable to download data from {link}")
        print("Attempting to download from api")
        return get_stock_from_api(search_company(company_name))


# Gets stock data for a company and parses it for calculation method
def get_and_parse_stock(company=None):
    if "http:" in company:
        name = "Name not available"
        try:
            temp = company.split(".csv")[0].split("/")
            name = temp[-1]
        except:
            print("Cannot retrieve company name from url")
        global company_name
        company_name = name
        return parse_data(get_content_from_link(company))
    else:
        return parse_data(get_stock_from_api(search_company(company)))


# Returns 2d list [[ABBREVIATION, description, category], etc]
def get_company_names():
    output = []
    try:
        with open("constituents_csv.csv", "r") as f:
            reader = csv.reader(f)
            for line in reader:
                output.append(line)
        return output[1:-1:]
    except IOError as e:
        print(e)
        print("Company name functionality lost, must use SYMBOL when searching for company")
        return output


# Returns ["SYMBOL", "Company name", "Category"]
def search_company(search_string):
    # Searching first for abbreviation
    for company in COMPANIES:
        if search_string.upper() == company[0]:
            return company
    for company in COMPANIES:
        if search_string.lower() in company[1].lower():
            return company

    return search_string.upper()


# Returns a 2d list in the format of [[Date, adj_close, volume], etc]
def parse_data(content):
    date_index, vol_index, adj_close_index = -1, -1, -1
    data = []
    if content:
        headers = content.split("\n")[0].split(",")
        for item in headers:
            if item == "Date" or item == "timestamp":
                date_index = headers.index(item)
            elif item == "Adj Close" or item == "adjusted_close":
                adj_close_index = headers.index(item)
            elif item.lower() == "volume":
                vol_index = headers.index(item)

        for row in content.split("\n")[1:-1:]:
            cells = row.strip().split(",")
            adj_close = make_nb_if_nb(cells[adj_close_index])
            volume = make_nb_if_nb(cells[vol_index])
            data.append([cells[date_index], adj_close, volume])

        return data


# Returns two lists with monthly and yearly averages [[DateOject, Value], etc]
def calculate_averages(data):
    """
    Calculates monthly and yearly averages
    Returns a tupple of 2d lists of monthly and yearly averages in form of [[DateObject, price], etc]
    :param data: [["date", "adj_close", "volume"],...]
    :return: (monthly_averages, yearly_averages)
    """
    # data = [["date", "adj_close", "volume"],...]
    if not data:
        print("Unable to download data \nExiting program")
        quit(1)
    monthly_average = []
    yearly_average = []

    curr_year = ""
    curr_month = ""
    month_temp = [0, 0]
    yearly_temp = [0, 0]
    for entry in data:

        if curr_month == "":     # Instantiates current month and year for the first line in the values
            curr_month = entry[0].split("-")[1]
            curr_year = entry[0].split("-")[0]

        if not curr_month == entry[0].split("-")[1]:  # New month has begun, calculating average and appending to list
            avg = month_temp[0] / float(month_temp[1])
            date_obj = dt.datetime.strptime(f"{curr_year}-{curr_month}-15", "%Y-%m-%d").date()
            monthly_average.append([date_obj, avg])
            month_temp = [0, 0]  # Resetting values for new current month
            curr_month = entry[0].split("-")[1]

        if not curr_year == entry[0].split("-")[0]:  # New year has begun, calculating average and appending it to list
            avg = yearly_temp[0] / float(yearly_temp[1])
            date_obj = dt.datetime.strptime(f"{curr_year}-07-01", "%Y-%m-%d").date()
            yearly_average.append([date_obj, avg])
            yearly_temp = [0, 0]  # Resetting values for new current year
            curr_year = entry[0].split("-")[0]

        # ((v1*c1)+(v2*c2)+(v3*c3)+(v4*c4)...+(vn*cn)) / (v1+v2+v3+v4...+vn)
        month_temp[0] += entry[2] * entry[1]  # volume * close
        month_temp[1] += entry[2]  # volume
        yearly_temp[0] += entry[2] * entry[1]
        yearly_temp[1] += entry[2]

    # Calculating and adding averages for last month and last year of the data set
    avg = yearly_temp[0] / float(yearly_temp[1])
    date_obj = dt.datetime.strptime(f"{curr_year}-07-01", "%Y-%m-%d").date()
    yearly_average.append([date_obj, avg])
    avg = month_temp[0] / float(month_temp[1])
    date_obj = dt.datetime.strptime(f"{curr_year}-{curr_month}-15", "%Y-%m-%d").date()
    monthly_average.append([date_obj, avg])

    return monthly_average, yearly_average


# Shows in console best and worst averages
def show_best_and_worst(averages, count=6):
    # Sorting the averages in descending order
    sorted_list = sorted(averages, key=lambda l: l[1], reverse=True)
    if count > len(averages):  # Making sure we do not try to get more items than we have in list
        count = len(averages)

    best = sorted_list[:count]  # First n entries are best ones
    worst = sorted_list[count*-1:]  # Last n entries are the worst
    worst.reverse()
    print_stats(best, worst)


# Plots a table with one or two 2d lists of averages [[DateObject, Value], etc]
def plot_data(*args):
    import matplotlib.pyplot as plt
    for param in args:  # Loops over parameters
        if param:  # Checks to see if params were provided
            x_data, y_data = [], []
            for item in param:
                x_data.append(item[0])
                y_data.append(item[1])

            label = "Yearly average" if param[0][0].day == 1 else "Monthly average"
            plt.plot(x_data, y_data, label=label)

    plt.ylabel('Stock price in USD')
    plt.title(company_name)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()


def print_stats(best_avg, worst_avg):
    description = "months" if best_avg[0][0].day == 15 else "years"
    print(f"\nBest {len(best_avg)} {description} \t\t\t\tWorst {len(best_avg)} {description}")
    for i in range(len(best_avg)):
        date_str = str(best_avg[i][0].year)
        date_str += f"-{best_avg[i][0].month}" if best_avg[i][0].day == 15 else ""
        print(f"{date_str}\t-> {best_avg[i][1]:.2f}", end="\t\t\t")
        date_str = str(worst_avg[i][0].year)
        date_str += f"-{worst_avg[i][0].month}" if worst_avg[i][0].day == 15 else ""
        print(f"{date_str}\t-> {worst_avg[i][1]:.2f}")


def main():
    DEFAULT_URL = "http://193.1.33.31:88/pa1/GOOGL.csv"
    query = input("Insert company name or link to csv file or leave blank for default ")
    if query == "":
        query = DEFAULT_URL

    monthly_average, yearly_average = calculate_averages(get_and_parse_stock(query))
    plot_data(monthly_average, yearly_average)  # requires pip install matplotlib
    show_best_and_worst(monthly_average, 6)
    show_best_and_worst(yearly_average, 6)


COMPANIES = get_company_names()


if __name__ == "__main__":
    main()
