from math import sqrt, pow


def closest_color(color, colorList):
    min_value = cartesian_distance(color, colorList[0][1])
    closest_color = colorList[0]
    for element in colorList:
        current_value = cartesian_distance(color, element[1])
        if(current_value < min_value):
            min_value = current_value
            closest_color = element
    return closest_color


def cartesian_distance(color, color2):
    r, g, b = hex_2_rgb(color)
    r2, g2, b2 = hex_2_rgb(color2)
    return sqrt(pow(r - r2, 2) + pow(g - g2, 2) + pow(b - b2, 2))


def hex_2_rgb(x):
    if len(x) == 4:
        return int(x[1]*2, 16), int(x[2]*2, 16), int(x[3]*2, 16)
    else:
        return int(x[1:3], 16), int(x[3:5], 16), int(x[5:], 16)
