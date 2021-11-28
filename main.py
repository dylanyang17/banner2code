class Format:
    C = 'c'


def add_margin(s, margin):
    return ' ' * 4 * margin + s


def get_start_string(fmt, margin=0):
    if fmt == Format.C:
        return add_margin('printf(\n', margin)


def get_end_string(fmt, margin=0):
    if fmt == Format.C:
        return add_margin(');', margin)


def convert(fmt, margin=0):
    """
    :param fmt: Convert to which format
    :param margin: How many "tabs" (actually spaces) before the first line
    :return:
    """
    with open('banner.txt', 'r') as f:
        lines = f.readlines()
    output = get_start_string(fmt, margin)
    for line in lines:
        if fmt == Format.C:
            line = '    "' + line.replace('\\', '\\\\').replace('%', '%%').replace('\n', '\\n') + '"'
        output += add_margin(line + '\n', margin + 1)
    output += get_end_string(fmt, margin)
    with open('code.txt', 'w') as f:
        f.write(output)


if __name__ == '__main__':
    convert(fmt='c', margin=1)
