def resolve(points=[], lines=(), circles=()):
    x_min = 1000
    x_max = -1000
    y_min = 1000
    y_max = -1000
    for line in lines:
        points.append((line[0], line[1]))
        points.append((line[2], line[3]))
    for point in points:
        if point[0] < x_min:
            x_min = point[0]
        if point[0] > x_max:
            x_max = point[0]
        if point[1] < y_min:
            y_min = point[1]
        if point[1] > y_max:
            y_max = point[1]
    for circle in circles:
        ray = circle[2]
        if circle[0] - ray < x_min:
            x_min = circle[0] - ray
        if circle[1] - ray < y_min:
            y_min = circle[1] - ray
        if circle[0] + ray > x_max:
            x_max = circle[0] + ray
        if circle[1] + ray > y_max:
            y_max = circle[1] + ray
    return '{0} {1} {2} {3}'.format(x_min, y_min, x_max, y_max)
