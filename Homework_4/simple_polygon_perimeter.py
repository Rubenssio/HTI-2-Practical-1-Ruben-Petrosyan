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


def simple_polygon_perimeter(points1):
    """
    Gets the coordinates of the points of a simple polygon, and returns the perimeter of that polygon

    Parameters
    ----------
    points1 : list
        A list of points as tuples. Each tuple containing the x and y coordinates of a point

    Returns
    -------
    float
        The perimeter of the simple polygon
    """

    perimeter = 0
    num_of_sides = len(points1)

    points2 = [points1[num_of_sides - 1], *points1[:num_of_sides - 1]]
    # points2 consists of the same points as 'points1' but each pair is shifted one position to the left in the list

    for j in range(num_of_sides):
        perimeter += segment_length(*points1[j], *points2[j])

    return perimeter


# THE MAIN PROGRAM
print("""\n    *** SIMPLE POLYGON PERIMETER CALCULATOR ***
Enter the coordinates of the simple polygon starting
from any point and by following the perimeter
""")
nums = [float(n) for n in input('Enter the coordinates x1 y1 x2 y2 etc...:\n').split()]

coordinates = []

# the following loop converts the list of floats into a list of tuples
# each tuple containing x and y float values of each point - [(x1, y1), (x2, y2), etc... ]
for i in range(len(nums)//2):
    coordinates.append((nums[i * 2], nums[i * 2 + 1]))

print('The perimeter is:', simple_polygon_perimeter(coordinates))
