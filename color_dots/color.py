from colr import color
from utils import sum_elements, get_sum_rgb, elem_func
from functools import lru_cache


class Color:

    @lru_cache(maxsize=120)
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, r, g, b):
        self.color = (r, g, b)

    def __repr__(self):
        return color('●', fore=self.color)

    def __eq__(self, other):
        if not isinstance(other, Color):
            print('Один из объектов - это не instance класса Color')
            return NotImplemented

        return self.color == other.color

    def __add__(self, other):
        if not isinstance(other, Color):
            print('Один из объектов - это не instance класса Color')
            return NotImplemented

        sum_color = sum_elements(self.color, other.color)
        new_rgb = get_sum_rgb(sum_color)
        return Color(*new_rgb)

    def __mul__(self, coef: float):
        cl = -256 * (1 - coef)
        f = 259 * (cl + 255) / (255 * (259 - cl))
        changed_color = elem_func(lambda x: f * (x - 128) + 128, self.color)
        return Color(*changed_color)

    def __rmul__(self, coef: float):
        cl = -256 * (1 - coef)
        f = 259 * (cl + 255) / (255 * (259 - cl))
        changed_color = elem_func(lambda x: f * (x - 128) + 128, self.color)
        return Color(*changed_color)


if __name__ == '__main__':
    # задание 1
    dot1 = Color(255, 0, 0)
    dot2 = Color(0, 255, 0)
    print(dot1, dot2)

    # задание 2
    print()
    print(dot1 == 'ghj')
    print(dot1 == Color(255, 0, 0))

    # задание 3
    print()
    print(dot1 + dot2)

    # задание 4
    print()
    print(dot1 * 0.5)
    print(0.5 * dot1)

    # задание 5
    print()
    dot3 = Color(0, 0, 255)
    dot4 = Color(0, 0, 255)
    print(dot3 is dot4)
