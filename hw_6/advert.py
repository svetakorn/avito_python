from colorize_mixin import ColorizeMixin


class Advert(ColorizeMixin):
    repr_color_code = 32  # green

    def __init__(self, data):
        if 'price' in data and data['price'] < 0:
            raise Exception('ValueError: must be >= 0')
        if 'class' in data:
            self.class_ = data['class']
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        """Рекурсивно преобразовывает вложенный словарь в объект"""
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return Advert(value) if isinstance(value, dict) else value

    def __getattr__(self, attr):
        """Действие при обращении к несуществующему атрибуту"""
        if attr == 'price':
            print('0')
