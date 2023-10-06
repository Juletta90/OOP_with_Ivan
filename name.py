from main import Person

j = Person("Julia", 33, "Moscow")
i = Person("Ivan", 39, "Moscow")

j.print()
i.print()

j.set_age(-3)   # на метанит - tom.age = -3486  # Недопустимый возраст   https://metanit.com/python/tutorial/7.2.php
i.set_age(1)    # т.е. знак "=" , а не в скобках с аргументом

j.get_age()
i.get_age()


# j.get_age(-3)
# i.get_age(1)