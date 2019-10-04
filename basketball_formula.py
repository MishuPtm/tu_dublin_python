"""
Take the number of points on team is ahead
Substract three
Add 1/2 point if team that is ahead has the ball or substract otherwise
Square the result
If the result is greater than the number of seconds left, the lead is safe
"""


def calculate_lead(lead_points, has_ball, seconds_left):
    value = lead_points - 3
    if has_ball:
        value += 0.5
    else:
        value -= 0.5

    if (value * value) > seconds_left:
        print(f"Winning with {lead_points} advantage and {seconds_left} seconds left")
        print(f"Avg seconds for every point = {seconds_left/lead_points}")
    else:
        print(f"Winning not garanteed")


calculate_lead(10, True, 50)
calculate_lead(5, True, 5)
calculate_lead(8, True, 50)
calculate_lead(7, True, 50)
calculate_lead(6, True, 50)
