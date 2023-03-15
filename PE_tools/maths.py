import pygame.math


def root_n(num, root=2):
    """mathematical root"""
    return num ** (1./root)


def fixed_float(num: float, num_of_zeros=3):
    """set the length of a float"""
    i = 10**num_of_zeros
    return int(num*i)/i


def fixed_int(num: int):
    """get the scientific name of a big number"""
    if num < 1000:
        return str(num)
    sci_code = ["K", "M", "B", "T", "qd", "Qt", "Sx", "Sp", "Oc", "N", "D", "A"]
    code = (len(str(num))-1)//3
    code -= 1
    if code > len(sci_code)-1:
        return "999+ A"
    new = f"{fixed_float(num/(10**(3*(code+1))), 2)}+ {sci_code[code]}"
    return new


def fixed_isnumeric(string: str, return_number=False, raise_error=False):
    """check if string is a number, even if its float or negative
    set return number to True to get an int in case of integer, float in case of float number
    or str in case of nan (Not A Number) string"""
    try:
        result = int(string)
    except ValueError:
        try:
            result = float(string)
        except ValueError:
            result = string
            if raise_error:
                raise ValueError(f"the string: '{string}' isn't a number!")
    if return_number:
        return result

    return type(result) == int or type(result) == float


class Bytes:
    """warning! PE bytes isn't python byte string. bytes set only made for saving data, and cant used as bytes string"""
    def __init__(self, length: int, base: int):
        self.Bytes = [0]*length
        self.base = base

    def total(self):
        """get the int value of the whole byte set"""
        tot = 0
        i = 0
        for x in self.Bytes:
            tot += x * self.base ** i
            i += 1
        return tot

    def set(self, value):
        """set the byte set to value"""
        b = self.Bytes
        for i in range(len(b)):
            b[i] = value // (self.base**i)
            b[i] = b[i] % self.base
        self.Bytes = b
        return b

    def change(self, value):
        """change the value of the byte set by number"""
        return self.set(self.total()+value)


class BaseN:
    """convert numbers between mathematical bases"""
    # functions
    def check_base(base: str):
        """check if a string is valid base"""
        dig = []
        for x in base:
            if x in dig:
                return False
            else:
                dig.append(x)
        return len(base) > 0

    def dec_to_base(num: int, base: str):
        """ translates number from int (base 10) into any base"""
        if not BaseN.check_base(base):
            raise ValueError(f"The string: {base} isn't a base")
            return None
        if num < 0:
            raise ValueError("negative numbers aren't supported yet")
            return None
        elif num == 0:
            return base[0]
        if base == "0123456789":
            return str(num)
        output = ""
        n = len(base)
        if n == 1:
            return base * num
        while num > 0:
            x = num
            num = num // n
            x = x % n
            output = base[x] + output
        return output

    def base_to_dec(num: str, base: str):
        """translate number from any base into int (base 10)"""
        if not BaseN.check_base(base):
            raise ValueError(f"The string: {base} isn't a base")
            return None
        if base == "0123456789":
            return int(num)
        output = 0
        n = len(base)
        i = len(num)
        for x in num:
            i -= 1
            if base.find(x) > -1:
                output += base.find(x) * (n**i)
            else:
                print(x)
                raise ValueError(
                    f"the number {num} cant be translated from base: {base}")
                return None
        return output

    def base_n(n: int):
        """returns the base of a number
        for example: base 2 = "01" or base 10 = "0123456789" """
        base = r"""
      0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`-=~!@#$%^&*()_+/\;:?[]{}.<>
      '"
      """
        base = base.replace("\n", "")
        base = base.replace("\t", "")
        base = base.replace(" ", "")
        if n > len(base) or n < 1:
            raise ValueError(
                f"The baseN: {n} must to be in range of: 1-{len(base)} ")
        return base[:n]


class TileMap (object):
    """great way to make a tile map, so usable in games, so now you can do it with pygame!"""
    def __init__(self, size: pygame.math.Vector2, fill=None):
        self.map = []
        for y in range(size[1]):
            self.map.append([])
            for x in range(size[0]):
                self.map[y].append(fill)

    def fill(self, fill=None):
        """fill the whole map with the same data.
        with no data, the map will cleared (fill all tiles with None Type)"""
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                self.map[y][x] = fill

    def get_tile(self, x, y=None):
        """get the value of a tile"""
        if isinstance(y, int):
            return self.map[y][x]
        else:
            return self.map[x[1]][x[0]]

    def set_tile(self, data, x, y=None):
        """set the value of a tile"""
        if y is not None:
            self.map[y][x] = data
        else:
            self.map[x[1]][x[0]] = data

    def get_size(self):
        """get the size of the tile in Vector 2"""
        return [len(self.map[0]), len(self.map)]


def float_in_range(num: float, num_range: range):
    """check if a float value is in range value"""
    return num >= num_range.start and num < num_range.stop


def string_in_range(num: str, num_range: range):
    """check if string is numeric and if so, in a range value.
    (using PE's fixed checks, so negative and floats work too)"""
    if not isinstance(num_range, range):
        return
    num = fixed_isnumeric(num, True)
    if isinstance(num, str):
        num = False
    if num:
        num = float_in_range(num, num_range)
    return num


class FixedRange:
    """this type of range working like regular python's range, but this can store even floats
    cant be used like regular range. all init parameters are numbers (None for making fast ranges like:
    start = 10, end = None, step = None : range(0, 10, 1)
    start = -5, end = 10, step = None: range(-5, 10, 1), and ect.)"""

    def __init__(self, start: float, end=None, step=None):
        if (start and end) and not step:
            if start > end:
                step = -1
            else:
                step = 1
        elif start and not (end and step):
            end = start
            start = 0
            step = 1

        self.start = start
        self.end = end
        self.step = step

    def py_range(self):
        """get the PE range as regular python's range (only ints)"""
        return range(int(self.start), int(self.end), int(self.step))

    def py_tuple(self, fix=True):
        """get as tuple, fix = True for fixing float"""
        if (self.start > self.end and self.step > 0) or self.step == 0 or (self.start < self.end and self.step < 0):
            return None
        i = self.start
        res = []
        if self.end < i:
            while i > self.end:
                if fix:
                    res.append(fixed_float(i, 3))
                else:
                    res.append(i)
                i += self.step

        else:
            while i < self.end:
                if fix:
                    res.append(fixed_float(i, 3))
                else:
                    res.append(i)
                i += self.step
        return tuple(res)
