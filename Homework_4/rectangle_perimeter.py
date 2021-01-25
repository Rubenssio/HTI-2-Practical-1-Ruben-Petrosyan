def segment_length(x1, y1, x2, y2):
    """
    Gets x and y coordinates of two points, and returns the distance between them

    Parameters
    ----------
    x1 : float
    y1 : float
        The x and y coordinates of the first point
    x2 : float
    y2 : float
        The x and y coordinates of the second point

    Returns
    -------
    float
        the distance between the first and second points
    """

    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


def rectangle_perimeter(points1):
    """
    Gets the coordinates of the points of the rectangle, and returns the perimeter of that rectangle

    Parameters
    ----------
    points1 : list
        A list of points as tuples. Each tuple containing the x and y coordinates of a point

    Returns
    -------
    float
        The perimeter of the rectangle
    """

    perimeter = 0
    points2 = [points1[3], *points1[:3]]  # same points as in 'points1' but shifted one position to the left in the list

    for j in range(4):
        perimeter += segment_length(*points1[j], *points2[j])

    return perimeter


# THE MAIN PROGRAM
nums = [float(n) for n in input('Enter the coordinates x1 y1 x2 y2 x3 y3 x4 y4: ').split()]

coordinates = []

# the following loop converts the list of floats into a list of tuples
# each tuple containing x and y float values of one point - [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
for i in range(len(nums)//2):
    coordinates.append((nums[i * 2], nums[i * 2 + 1]))

print('The perimeter is:', rectangle_perimeter(coordinates))
