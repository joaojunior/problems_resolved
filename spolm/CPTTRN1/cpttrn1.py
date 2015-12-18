import sys

def resolve(lines, collumns):
    result = ''
    for line in xrange(lines):
        for collumn in xrange(collumns):
            rest = (line + collumn) % 2
            if rest == 0:
                result += '*'
            else:
                result += '.'
        if line + 1 < lines:
            result += '\n'
    return result

if __name__ == '__main__':
    numbers_tests = int(sys.stdin.next())
    for line in sys.stdin:
        line = line.split()
        lines = int(line[0])
        collumns = int(line[1])
        print resolve(lines, collumns)
