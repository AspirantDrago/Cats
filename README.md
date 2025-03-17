# Дисциплина **Разработка и поддержка программных модулей**

Используйте библиотеку `doctest` для написания unit-тестов
*(писать саму документацию не обязательно)*.

## Задание по вариантам:

| №  | ФИО              | файл               | метод / геттер                               |
|:--:|------------------|--------------------|--------------------------------------------------------|
| 1  | Абдукадыров Д.Х. | `game/cat.py`      | `Cat.__eq__(self, other: 'Cat') -> bool`               |
| 2  | Алимгулов А.У.   | `game/cat.py`      | `@property Cat.gender(self) -> Gender`                 |
| 3  | Бикметов Э.И.    | `game/cat.py`      | `@property Cat.color(self) -> Color`                   |
| 4  | Валиев Э.А.      | `game/cat.py`      | `@property Cat.age(self) -> int`                       |
| 5  | Егоров П.С.      | `game/cat.py`      | `@property Cat.hungry(self) -> bool`                   |
| 6  | Каримов Д.С.     | `game/cat.py`      | `@property Cat.is_adult(self) -> bool`                 |
| 7  | Костин С.С.      | `game/cat.py`      | `@property Cat.is_chpock(self) -> bool`                |
| 8  | Машарипов Ш.М    | `game/cat.py`      | `Cat.new_season(self) -> None`                         |
| 9  | Мухаммадиев С.А. | `game/cat.py`      | `Cat.__repr__(self) -> str:`                           |
| 10 | Нурлыгаянов Э.И. | `game/cat.py`      | `Cat.__str__(self) -> str`                             |
| 11 | Петрухан Е.А.    | `game/cat.py`      | `Cat.clone(self) -> Cat`                               |
| 12 | Рахматуллин А.Ю. | `game/home.py`     | `Home.__getitem__(self, item: int) -> Room`            |
| 13 | Рымарева А.Н.    | `game/magazine.py` | `@property Magazine.name(self) -> str`                 |
| 14 | Сайфуллин Т.А.   | `game/magazine.py` | `@property Magazine.offers(self) -> tuple[Offer, ...]` |
| 15 | Хамрабаев О.О.   | `game/magazine.py` | `Magazine.__str__(self) -> str`                        |
| 16 | Хасанова Э.М.    | `game/magazine.py` | `Magazine.__repr__(self) -> str`                       |

## Формат ответа

В качестве решения можете отправить `doc` или `pdf`-документ, в котором укажите:
- Код своей функции/метода
- `docstring` с написанными тестами
- скриншот с прохождением тестов

Напишите тесты так, чтобы продемонстрировать и проверить все сценарии работы метода.

## Примеры тестов в файле `./game/cat.py`:

```python
class Cat(SeasonMixin):
    ...

    def __mul__(self, other: 'Cat') -> list['Cat']:
        """
        Метод "умножения" двух котов.
        Отвечает за скрещивание двух котов и генерацию потомства.
        Если животные одного пола, то выбрасывается исключение ErrorOneGenderChpock

        :param other: Вторая кошка, скрещиваемая с текущей
        :return: Список котят
        :raise ErrorOneGenderChpock:

        >>> cat1 = Cat(Gender.MALE, Color.LIGHT)
        >>> cat2 = Cat(Gender.FEMALE, Color.DARK)
        >>> cat1 * cat2
        [Cat MALE LIGHT 0, Cat MALE LIGHT 0, Cat FEMALE LIGHT 0, Cat MALE DARK 0, Cat MALE DARK 0, Cat FEMALE DARK 0]

        >>> cat3 = Cat(Gender.MALE, Color.LIGHT)
        >>> cat1 * cat3
        Traceback (most recent call last):
            ...
        cat.ErrorOneGenderChpock: один пол: MALE и MALE

        """
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

    def feed(self) -> None:
        """

        >>> cat = Cat(Gender.FEMALE, Color.LIGHT)
        >>> cat.new_season()
        >>> cat.hungry
        True
        >>> cat.feed()
        Traceback (most recent call last):
            ...
        game.user.ErrorNoMoney
        >>> from game.user import User
        >>> User.get().money += 1
        >>> cat.feed()
        >>> cat.hungry
        False
        """
        if self._hungry:
            from game.user import User

            self._hungry = False
            User.get().money -= 1


if __name__ == '__main__':
    doctest.testmod()

```
