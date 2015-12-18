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
