from .cat import Cat


class ErrorCatNotFound(Exception):
    pass


class Offer:
    """
    Объявление о покупке/продаже
    """

    def __init__(self,
                 cat: Cat,
                 price_buy: int,
                 price_sell: int,
                 ):
        self._cat = cat
        self._price_buy = price_buy
        self._price_sell = price_sell

    @property
    def cat(self) -> Cat:
        return self._cat

    @property
    def price_buy(self) -> int:
        return self._price_buy

    @property
    def price_sell(self) -> int:
        return self._price_sell

    def buy(self) -> None:
        from .user import User

        User.get().money -= self._price_sell
        User.get().cats.append(self._cat.clone())

    def sell(self) -> None:
        from .user import User

        if self._cat not in User.get().cats:
            raise ErrorCatNotFound(f'{self._cat} not found!')
        User.get().cats.remove(self._cat)
        User.get().money += self._price_buy

    def __str__(self) -> str:
        return f'{self._cat.gender} {self._cat.color} buy={self._price_buy} sell={self._price_sell}'
