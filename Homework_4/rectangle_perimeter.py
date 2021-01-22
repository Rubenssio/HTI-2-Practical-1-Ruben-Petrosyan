def segment_length(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


def rectangle_perimeter(points1):
    perimeter = 0
    points2 = [points1[3], *points1[:3]]

    for i in range(4):
        perimeter += segment_length(*points1[i], *points2[i])

    return perimeter


nums = [float(n) for n in input('Enter coordinates x1 y1 x2 y2 x3 y3 x4 y4: ').split()]
coordinates = []
for i in range(len(nums)//2):
    coordinates.append((nums[i * 2], nums[i * 2 + 1]))

print(rectangle_perimeter(coordinates))
