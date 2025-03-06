from enum import Enum

from ._utils import SeasonMixin


class Gender(Enum):
    MALE = 1
    FEMALE = 2

    def __str__(self) -> str:
        return self.name


class Color(Enum):
    LIGHT = 1
    DARK = 2

    def __str__(self) -> str:
        return self.name


class ErrorCat(Exception):
    ...


class ErrorLossCat(ErrorCat):
    ...


class ErrorOneGenderChpock(ErrorCat):
    ...


class Cat(SeasonMixin):
    def __init__(self,
                 gender: Gender,
                 color: Color,
                 ):
        self._gender = gender
        self._color = color
        self._age = 0
        self._hungry = False

    def __eq__(self, other: 'Cat') -> bool:
        if not isinstance(other, Cat):
            return False
        if self._gender != other._gender:
            return False
        if self._color != other._color:
            return False
        if self._age != other._age:
            return False
        # if self._hungry != other._hungry:
        #     return False
        return True

    @property
    def gender(self) -> Gender:
        return self._gender

    @property
    def color(self) -> Color:
        return self._color

    @property
    def age(self) -> int:
        return self._age

    @property
    def hungry(self) -> bool:
        return self._hungry

    @property
    def is_adult(self) -> bool:
        return self._age >= 3

    @property
    def is_chpock(self) -> bool:
        return not self._hungry and self.is_adult

    def new_season(self) -> None:
        if self.hungry:
            raise ErrorLossCat("Hungry cat lossed")
        self._age += 1
        self._hungry = True

    def __mul__(self, other: 'Cat') -> list['Cat']:
        if self.gender == other.gender:
            raise ErrorOneGenderChpock(f"один пол: {self.gender} и {other.gender}")
        return [
            Cat(Gender.MALE, self.color),
            Cat(Gender.MALE, self.color),
            Cat(Gender.FEMALE, self.color),
            Cat(Gender.MALE, other.color),
            Cat(Gender.MALE, other.color),
            Cat(Gender.FEMALE, other.color),
        ]

    def __repr__(self) -> str:
        return f'Cat {self._gender} {self._color} {self._age}'

    def __str__(self) -> str:
        return f'Cat {self._gender} {self._color} {self._age}'

    def clone(self) -> 'Cat':
        c = Cat(
            self._gender,
            self._color,
        )
        c._age = self._age
        c._hungry = self._hungry
        return c

    def feed(self) -> None:
        if self._hungry:
            from .user import User

            self._hungry = False
            User.get().money -= 1
