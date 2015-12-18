def resolve(lines, collumns):
    result = ''
    for line in xrange(lines):
        for collumn in xrange(collumns):
            line_rest = line % 2
            collumn_rest = collumn % 2
            if line_rest == 0 and collumn_rest == 0:
                result += '*'
            elif line_rest == 0 and collumn_rest != 0:
                result += '.'
            elif line_rest != 0 and collumn_rest == 0:
                result += '.'
            elif line_rest != 0 and collumn_rest != 0:
                result += '*'
        if line + 1 != lines:
            result += '\n'
    return result
