def segment_length(x1, y1, x2, y2):
    import math  # ակնկալում եմ այս ֆունկցիան իրականացնել առանց math import անելու

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def rectangle_perimeter(points1):
    perimeter = 0
    points2 = [points1[3], *points1[:3]]

    for i in range(4):
        perimeter += segment_length(*points1[i], *points2[i])

    return perimeter


coordinates = []
for i in range(4):
    point_x_y = tuple(float(n) for n in input(f'Enter coordinates of x{i + 1} and y{i + 1}: ').split())
    coordinates.append(point_x_y)

print(rectangle_perimeter(coordinates))
