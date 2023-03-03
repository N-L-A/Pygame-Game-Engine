from PE_tools.maths import fixed_isnumeric


def write(dir: str, list: list):
    """save a list on the drive as PE's list file"""
    l = ""
    for x in list:
        l = l + str(x)
        l = l + "\n"
    open(dir, 'w').write(l)


def read(dir: str, auto_convert=True):
    """read data from PE's list file
    set auto_convert to False to get numbers as strings"""
    t = open(dir, 'r').read()
    l = []
    y = ""
    for x in enumerate(t):
        x = x[1]
        if x == '\n':
            if auto_convert:
                l.append(fixed_isnumeric(y, True))
            else:
                l.append(y)
            y = ""
        else:
            y = y + x
    return l

