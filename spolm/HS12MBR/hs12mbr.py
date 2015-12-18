def resolve(points=(), lines=(), circles=()):
    x_min = 1000
    x_max = -1000
    y_min = 1000
    y_max = -1000
    points = list(points)
    for line in lines:
        points.append((line[0], line[1]))
        points.append((line[2], line[3]))
    for circle in circles:
        ray = circle[2]
        points.append((circle[0] - ray, circle[1] - ray))
        points.append((circle[0] + ray, circle[1] + ray))
    for point in points:
        if point[0] < x_min:
            x_min = point[0]
        if point[0] > x_max:
            x_max = point[0]
        if point[1] < y_min:
            y_min = point[1]
        if point[1] > y_max:
            y_max = point[1]
    return '{0} {1} {2} {3}'.format(x_min, y_min, x_max, y_max)
