from game import *

User(18)
offers_Бонифаций = [
        Offer(Cat(Gender.MALE, Color.DARK), 3, 4),
        Offer(Cat(Gender.FEMALE, Color.DARK), 3, 4),
        Offer(Cat(Gender.MALE, Color.LIGHT), 4, 5),
        Offer(Cat(Gender.FEMALE, Color.LIGHT), 5, 6),
    ]
User.get().magazines = [
    Magazine('Бонифаций', offers_Бонифаций)
]
offers_Бонифаций[1].buy()
offers_Бонифаций[2].buy()
User.get().homes.append(Home())
User.get().homes[0][0].cat_1 = User.get().cats[0]
User.get().homes[0][0].cat_2 = User.get().cats[0]
for _ in range(3):
    User.get().new_season()
    User.get().feed_all()
User.get().homes[0][0].chpock()
for _ in range(6):
    User.get().sell_by_index(0)

print(User.get())