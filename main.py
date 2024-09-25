#Для реализации данной задачи с применением принципа открытости / закрытости, мы
# создадим абстрактный класс `Weapon`, конкретные классы оружия, и
# модифицируем класс `Fighter` для поддержки смены оружия.Ниже
# приведен пример кода на Python:

# ```python
from abc import ABC, abstractmethod


# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def fight(self):
        return self.weapon.attack()


# Класс Monster, представляющий монстра
class Monster:
    def __init__(self, health: int):
        self.health = health

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            return "Монстр побежден!"
        else:
            return f"У монстра осталось {self.health} здоровья."


# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    print(fighter.fight())
    print(monster.take_damage(10))  # Допустим, каждая атака наносит 10 единиц урона


# Пример использования
if __name__ == "__main__":
    sword = Sword()
    bow = Bow()

    fighter = Fighter(sword)
    monster = Monster(10)

    print("Боец выбирает меч.")
    battle(fighter, monster)

    # Меняем оружие на лук
    fighter.changeWeapon(bow)
    monster = Monster(10)  # Новый монстр для демонстрации

    print("Боец выбирает лук.")
    battle(fighter, monster)
#```

### Объяснение:

#1. ** Абстрактный класс `Weapon`: ** Определяет интерфейс для
#всех видов оружия с методом `attack()`.

#2. ** Конкретные классы оружия: ** `Sword` и `Bow` реализуют
#метод `attack()` по - разному.Это позволяет добавлять новые
#виды оружия без изменения существующих классов.

# 3. ** Класс `Fighter`: ** Имеет поле для хранения объекта типа
# `Weapon` и метод `changeWeapon()` для смены оружия.

# 4. ** Механизм боя: ** Функция `battle` демонстрирует взаимодействие
# между бойцом и монстром. Она использует метод `fight()` бойца, чтобы
# выполнить атаку, и метод `take_damage()` монстра, чтобы обработать
# нанесенный урон.

# Этот подход позволяет легко добавлять новые виды оружия, просто
# создавая новые классы, наследующие от `Weapon`, без изменения
# `Fighter` или механизма боя, что демонстрирует принцип
# открытости/закрытости.