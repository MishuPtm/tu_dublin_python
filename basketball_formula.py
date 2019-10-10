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
        print("The lead is safe")
    else:
        print("Winning is not guaranteed")



