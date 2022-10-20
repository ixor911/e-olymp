class Constants:
    def __init__(self):
        self.a = 12
        self.b = 8
        self.c = 5
        self.d = 3


const = Constants()


def calc_full_cube(k):
    return const.a + 3 * (k - 1) * const.b + 3 * pow((k - 1), 2) * const.c + pow((k - 1), 3) * const.d


def calc_full_square(k):
    return const.b + 2 * (k - 1) * const.c + pow((k - 1), 2) * const.d


def calc_edge(k):
    return const.c + (k - 1) * const.d


def calc_not_full_cube(x, y, z):
    min_cube = calc_full_cube(z)
    side1 = 0
    side2 = 0
    edge = 0

    if x > z:
        side1 = calc_full_square(z)

    if y > z:
        side2 = calc_full_square(z)

    if y > z and x > z:
        edge = calc_edge(z)

    return min_cube + side2 + side1 + edge


def calc_not_full_edge(left):
    return const.c + const.d * left


def calc_not_full_square(x, y, left):
    min_value = min(x, y)
    small_square = 0
    side1 = 0
    side2 = 0

    if left > min_value * min_value:
        small_square = calc_full_square(min_value)
        left -= min_value * min_value

        if left >= min_value:
            side1 = calc_edge(min_value)
            left -= min_value
        elif 0 < left < min_value:
            side2 = calc_not_full_edge(left)
            left = 0

        if left >= min_value:
            side2 = calc_edge(min_value)
            left -= min_value
        elif 0 < left < min_value:
            side2 = calc_not_full_edge(left)
            left = 0

    elif left == min_value * min_value:
        small_square = calc_full_square(min_value)
    else:
        small_square = calc_not_full_square(min_value - 1, min_value - 1, left)

    return small_square + side1 + side2


def start():
    n = int(input())

    if n <= 0:
        print(0)
    elif n == 1:
        print(12)
    elif 1 < n < 8:
        side1 = 0
        side2 = 0

        if n >= 4:
            side1 = 12 + 8 + 8 + 5
            if n > 4:
                side2 = 8 + 5 * (n - 5)
        else:
            side1 = 12 + 8 * (n - 1)

        print(side2 + side1)

    elif n == 8:
        print(calc_full_cube(2))

    elif n > 8:
        i = 2
        while pow(i, 3) < n:
            i += 1

        not_full_cube = 0
        not_full_square = 0

        if pow(i, 3) == n:
            not_full_cube = calc_full_cube(i)

        elif i * i * (i - 1) < n < pow(i, 3):
            left = n - i * i * (i - 1)
            not_full_cube = calc_not_full_cube(i, i, i - 1)
            not_full_square = calc_not_full_square(i, i, left)

        elif i * (i - 1) * (i - 1) < n <= i * i * (i - 1):
            left = n - i * (i - 1) * (i - 1)
            not_full_cube = calc_not_full_cube(i, i - 1, i - 1)
            not_full_square = calc_not_full_square(i, i - 1, left)

        elif (i - 1) * (i - 1) * (i - 1) < n <= i * (i - 1) * (i - 1):
            left = n - (i - 1) * (i - 1) * (i - 1)
            not_full_cube = calc_full_cube(i - 1)
            not_full_square = calc_not_full_square(i - 1, i - 1, left)

        print(not_full_cube + not_full_square)








