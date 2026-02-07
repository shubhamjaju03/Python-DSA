def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    arrows = 1
    last_end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > last_end:
            arrows += 1
            last_end = points[i][1]

    return arrows
