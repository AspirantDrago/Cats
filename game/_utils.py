from abc import ABCMeta, abstractmethod


class SeasonMixin(metaclass=ABCMeta):
    @abstractmethod
    def new_season(self):
        ...
