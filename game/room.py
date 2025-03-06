from typing_extensions import override

from ._utils import SeasonMixin
from .cat import Cat


class ErrorRoomBusy(Exception):
    ...


class Room(SeasonMixin):
    def __init__(self, number: int):
        self._cat_1: Cat | None = None
        self._cat_2: Cat | None = None
        self._number: int = number

    @property
    def cat_1(self) -> Cat | None:
        return self._cat_1

    @property
    def cat_2(self) -> Cat | None:
        return self._cat_2

    @cat_1.setter
    def cat_1(self, value: Cat | None) -> None:
        if self._cat_1 is not None and value is not None:
            raise ErrorRoomBusy(f'In room {self._number} cat 1 exists')
        if value is not None:
            from .user import User

            User.get().cats.remove(value)
        self._cat_1 = value

    @cat_2.setter
    def cat_2(self, value: Cat | None) -> None:
        if self._cat_2 is not None and value is not None:
            raise ErrorRoomBusy(f'In room {self._number} cat 2 exists')
        if value is not None:
            from .user import User

            User.get().cats.remove(value)
        self._cat_2 = value

    def chpock(self) -> None:
        if self._cat_1 is None:
            return
        if self._cat_2 is None:
            return
        from .user import User

        kittens = self._cat_1 * self._cat_2
        User.get().cats.extend(kittens)

    @override
    def new_season(self):
        if self._cat_1 is not None:
            self._cat_1.new_season()
        if self._cat_2 is not None:
            self._cat_2.new_season()

    def feed(self):
        if self._cat_1 is not None and self._cat_1.hungry:
            self._cat_1.feed()
        if self._cat_2 is not None and self._cat_2.hungry:
            self._cat_2.feed()
