import sys

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

if __name__ == '__main__':
    numbers_tests = int(sys.stdin.next())
    for test in xrange(numbers_tests):
        quantity = int(sys.stdin.next())
        points = []
        lines = []
        circles = []
        for i in xrange(quantity):
            line = sys.stdin.next()
            line = line.split()
            if line[0] == 'p':
                points.append((int(line[1]), int(line[2])))
            elif line[0] == 'l':
                lines.append((int(line[1]), int(line[2]), int(line[3]), int(line[4])))
            elif line[0] == 'c':
                circles.append((int(line[1]), int(line[2]), int(line[3])))
        print resolve(points, lines, circles)
        if test + 1 < numbers_tests:
            sys.stdin.next()
