from typing import override

from ._utils import SeasonMixin
from .room import Room


class Home(SeasonMixin):
    _count = 0
    PRICE = 3

    def __init__(self, count_rooms=2):
        from .user import User

        Home._count += 1
        self._number = Home._count
        self._count_rooms = count_rooms
        self._rooms = [
            Room(i + 1)
            for i in range(count_rooms)
        ]
        User.get().money -= Home.PRICE

    @override
    def new_season(self):
        for room in self._rooms:
            room.new_season()

    def __getitem__(self, item: int) -> Room:
        return self._rooms[item]

    def feed(self) -> None:
        for room in self._rooms:
            room.feed()
