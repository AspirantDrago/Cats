from typing import Optional, override

from ._utils import SeasonMixin
from .cat import Cat
from .home import Home
from .magazine import Magazine


class ErrorNoMoney(Exception):
    ...


class ErrorOfferNotFound(Exception):
    ...


class User(SeasonMixin):
    _instance: Optional['User'] = None

    def __init__(self, money=0):
        self._money = money
        self.cats: list[Cat] = []
        User._instance = self
        self.magazines: list[Magazine] = []
        self.homes: list[Home] = []

    @staticmethod
    def get() -> 'User':
        if User._instance is None:
            User._instance = User()
        return User._instance

    @property
    def money(self) -> int:
        return self._money

    @money.setter
    def money(self, money: int) -> None:
        if money < 0:
            raise ErrorNoMoney
        self._money = money

    @override
    def new_season(self):
        for cat in self.cats:
            cat.new_season()
        for home in self.homes:
            home.new_season()

    def __str__(self) -> str:
        return f'''У нас монет: {self._money}
        Кошки: {self.cats}'''

    def feed_all(self) -> None:
        for cat in self.cats:
            cat.feed()
        for home in self.homes:
            home.feed()

    def sell_by_index(self, index) -> None:
        cat = self.cats[index]
        best_offer = None
        for mazazine in self.magazines:
            for offer in mazazine.offers:
                if offer.cat == cat:
                    if best_offer is None or offer.price_buy > best_offer.price_buy:
                        best_offer = offer
        if best_offer is None:
            raise ErrorOfferNotFound(f'Offer not found for {cat}')
        best_offer.sell()
