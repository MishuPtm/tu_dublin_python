Data mining is the process of sorting through large amounts of data and picking out relevant information.
In this assignment we want to do some preliminary data mining of a company's stock.
This sort of data is available from finance.yahoo.com, where you can, among other things,
search historical data by company. For this assignment we'll look at Google from 2004 to date (Oct 2019).
The data-set you'll need is in CSV format and can be accessed on http://193.1.33.31:88/pa1/GOOGL.csv.
The data has a header line giving the column names.

Your program should calculate the monthly and yearly average price for Google
and tell us the best and worst six months and the best and worst six years for Google.

The average price is defined as ((v1*c1)+(v2*c2)+(v3*c3)+(v4*c4)...+(vn*cn)) / (v1+v2+v3+v4...+vn)
where vi is the volume for day i and ci is the adjusted close price for day i.