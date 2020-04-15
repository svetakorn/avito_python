class ColorizeMixin:
    repr_color_code = 34

    def __repr__(self):
        return f"\033[1;{self.repr_color_code};46m{self.title} | {self.price} ₽"
