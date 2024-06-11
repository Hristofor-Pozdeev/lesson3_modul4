# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement make_sound method")

    def eat(self):
        print(f"{self.name} is eating...")

# Подклассы
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} tweets.")

class Mammal(Animal):
    pass  # Здесь можно добавить специфические атрибуты и методы

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} hisses.")

# Полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Пример использования
dodo = Bird('Dodo', 10)
turtle = Reptile('Turtle', 5)
animal_sound([dodo, turtle])



# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} feeds {animal.name}")

# Класс Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} heals {animal.name}")

# Класс Employee (общий класс для сотрудников)
class Employee:
    def __init__(self, name):
        self.name = name

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

# Пример использования
zoo = Zoo()
keeper = ZooKeeper("John")
vet = Veterinarian("Sarah")
bird = Bird("Tweety", 5)

zoo.add_animal(bird)
zoo.add_employee(keeper)
zoo.add_employee(vet)

keeper.feed_animal(bird)
vet.heal_animal(bird)





