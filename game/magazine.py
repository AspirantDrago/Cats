from game.offer import Offer


class Magazine:
    def __init__(self, name: str, offers: list[Offer]):
        self._name = name
        self._offers = tuple(offers)

    @property
    def name(self) -> str:
        return self._name

    @property
    def offers(self) -> tuple[Offer, ...]:
        return self._offers

    def __str__(self) -> str:
        text = [f'Magazine "{self._name}":']
        for offer in self._offers:
            text.append('\t' + str(offer))
        return '\n'.join(text)

    def __repr__(self) -> str:
        return self.__str__()
