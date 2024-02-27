import math

def distance_point_line(a, b, c, x, y):
    """describes the distance between a line and a point

    This is the distance between a point and a line with the help of the line equation:
    0 = ax + by + c
    which translates to the well known form of the line equation:
    y = mx + c
    You translate the one to the other through writing "by" to the 0 side of the equation and
    divide by b.
    Then you have the slope with (a/b) and the y offset with (c/b).
    The distance is calculated by:
    |ax_0 + by_0 + c|
    -----------------  = distance
     sqrt(a^2 + b^2)

    Args:
        a (coefficient for x): a is the coefficient for x for the line equation 0 = ax + by + c
        b (coefficient for y): b is the coefficient for y for the line equation 0 = ax + by + c
        c (remainder): c is the remainder to get the 0 one the one side of the equation
        x (x coordinate): x coordinate of the point at hand
        y (y coordinate): y coordinate of the point at hand
    """
    return abs(a * x + b * y + c) / math.sqrt(a**2 + b**2)
