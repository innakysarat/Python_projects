import json
from keyword import iskeyword


class JsonConverter:
    def __init__(self, data: dict):
        for attr, value in data.items():
            if iskeyword(attr):
                attr += "_"
            if isinstance(value, dict):
                setattr(self, attr, JsonConverter(value))
            else:
                setattr(self, attr, value)


class ColorizeMixin:
    def __repr__(self) -> str:
        return f"\033[1;{self.repr_color_code};40m{self.title} | {self.price} ₽"


class Advert(JsonConverter, ColorizeMixin):
    repr_color_code = 32

    def __init__(self, data: dict):
        super().__init__(data)
        if not hasattr(self, "title"):
            raise KeyError("Field title should be present")
        if not hasattr(self, "price"):
            self._price = 0

    def __repr__(self) -> str:
        return super().__repr__()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price should be >=0")
        self._price = price


if __name__ == '__main__':
    lesson_str = """{
         "title": "python",
         "price": 0,
         "location": {
             "address": "город Москва, Лесная, 7",
             "metro_stations": ["Белорусская"]
             }
         }"""
    corgi_str = """{
         "title": "Вельш-корги",
         "price": 1000,
         "class": "dogs",
         "location": {
             "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
             }
         }"""
    lesson_ad = Advert(json.loads(lesson_str))
    corgi = Advert(json.loads(corgi_str))
    print(lesson_ad.location.address)
    print(lesson_ad.price)
    print(corgi.class_)
    print(corgi)