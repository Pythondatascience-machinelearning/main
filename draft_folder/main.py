# from collections import namedtuple
# Point = namedtuple('Point',['x','y'])
# p=Point(11, y=22)
# print(p.x)
# print(p.y)

# import collections


# Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
# print(person.first_name)
# print(person.last_name)
# print(person.age)
# print(person[3])

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark]+=1
#     # else: 
#     #     mark_counts[mark]=1
# print(mark_counts)

# import collections
# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)
# print(mark_counts.most_common())
# print(mark_counts.most_common(2))

# from collections import Counter

# letter= """Наприклад, якщо вам потрібно підрахувати кількість кожної літери у рядку, 
# просто передайте рядок безпосередньо до Counter. Тоді ви можете легко отримати 
# доступ до кількості кожної літери за допомогою ключів, як у звичайному словнику."""
# letters=Counter(letter)
# print(letters)
# words=letter.split()
# word_counter=Counter(words)
# print(word_counter)

# from collections import defaultdict

# # Створення defaultdict з list як фабрикою за замовчуванням
# d = defaultdict(list)

# # Додавання елементів до списку для кожного ключа
# d['a'].append(1)
# d['a'].append(3)
# d['d'].append(5)
# d['b'].append(4)

# print(d)

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}
# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#          grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)

# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(dict(grouped_words))
# print(grouped_words)

# def creat_stack():
#     return[]
# def is_empty(stack):
#     return len(stack) == 0
# def push(stack, item):
#     stack.append(item)
# def pop(stack):
#     if not is_empty(stack):
#         return stack.pop()
#     else:
#         print("Стек порожній")
# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else:
#         print("Stack is empty")
# stack= creat_stack()
# push(stack, "a")
# push(stack, "b")
# push(stack,"c")

# print(peek(stack))
# print(pop(stack))
# print(peek(stack))
# from collections import deque

# d = deque()
# for i in range(10):
#     d.append(i)

# print(d)

# from collections import deque

# # Список завдань, де кожне завдання - це словник
# tasks = [
#     {"type": "fast", "name": "Помити посуд"},
#     {"type": "slow", "name": "Подивитись серіал"},
#     {"type": "fast", "name": "Вигуляти собаку"},
#     {"type": "slow", "name": "Почитати книгу"}
# ]

# # Ініціалізація черги завдань
# task_queue = deque()

# # Розподіл завдань у чергу відповідно до їх пріоритету
# for task in tasks:
#     if task["type"] == "fast":
#         task_queue.appendleft(task)  # Додавання на високий пріоритет
#         print(f"Додано швидке завдання: {task['name']}")
#     else:
#         task_queue.append(task)  # Додавання на низький пріоритет
#         print(f"Додано повільне завдання: {task['name']}")

# # Виконання завдань
# while task_queue:
#     task_queue.append({"type": "fast", "name": "1"})
#     print(f"Виконується завдання: {task['name']}")

# from decimal import Decimal 

# print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
# print(Decimal("0.1") + Decimal("0.2"))

# from decimal import getcontext
# getcontext().prec= 4
# from decimal import Decimal, getcontext

# getcontext().prec = 6
# print(Decimal("1") / Decimal("7"))

# getcontext().prec = 8
# print(Decimal("1") / Decimal("7"))

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()

# # Використання next()
# print(next(gen))  # Виведе 1
# print(next(gen))  # Виведе 2
# print(next(gen))

# def count_down(start):
#     while start > 0:
#         yield start
#         start -=1
# for number in count_down(100):
#     print(number)

# def my_function():
#     print("Hello, world!")

# f = my_function
# print(f"{f()}")

# from typing import Callable

# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner

# # Використання
# square = power(2)
# cube = power(3)

# print(square(4)) 
# print(cube(4))

# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)

#     return inner_function

# # Створення замикання
# my_func = outer_function("Hello, world!")
# my_func()

# from typing import Callable

# def counter() -> Callable[[], int]:
#     count = 0

#     def increment() -> int:
#         # використовуємо nonlocal, щоб змінити змінну в замиканні
#         nonlocal count  
#         count += 1
#         return count

#     return increment

# # Створення лічильника
# count_calls = counter()

# # Виклики лічильника
# print(count_calls())  # Виведе 1
# print(count_calls())  # Виведе 2
# print(count_calls())  # Виведе 3

# def add(a):
#     def add_b(b):
#         return a + b
#     return add_b

# # Використання:
# add_5 = add(5)
# result = add_5(10)
# print(result)
# from typing import Callable, Dict

# def discount(discount_percentage: int) -> Callable[[float], float]:
#     def apply_discount(price: float) -> float:
#         return price * (1 - discount_percentage / 100)
#     return apply_discount

# # Створення словника з функціями знижок
# discount_functions: Dict[str, Callable] = {
#     "10%": discount(10),
#     "20%": discount(20),
#     "30%": discount(30)
# }

# # Використання функції зі словника
# price = 500
# discount_type = "20%"

# discounted_price = discount_functions[discount_type](price)
# print(f"Ціна зі знижкою {discount_type}: {discounted_price}")

# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y

# print(complicated(2, 3))

# /////////////////////////
# def complicated(x: int, y: int) -> int:
#     return x + y

# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# complicated = logger(complicated)
# print(complicated(2, 3))

# from functools import wraps

# def logger(func):
#     @wraps(func)
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner

# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y

# print(complicated(2, 3))
# print(complicated.__name__)


# sq = {x:x**2 for x in range (1,10) if x**2 >10}
# print(sq)

# add = lambda x, y: x+y
# print(add(5,3))

# nums = [1,2,3,4,5]
# nums_sorted = sorted( nums, key= lambda x:-x)
# print(nums_sorted)

# nums = [1,2,3,4,5]
# nums_sorted = sorted( nums, key= None, reverse = True)
# print(nums_sorted)

# nums = [1,2,3,4,5]
# for i in map(lambda x:x*2, nums):
#    print(i)

# nums = [1,2,3,4,5]
# squared_nums = list(map(lambda x: x**2, nums))
# print(squared_nums)

# nums1 = [1,2,3]
# nums2 = [4,5,6]
# squared_nums = list(map(lambda x,y:x*y, nums1, nums2))  
# print(squared_nums)


# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# squared_nums = list(map(lambda x, y: x * y, nums1, nums2))  
# print(squared_nums)

# nums = [1,2,3,4,5,6]
# squared_nums = [x*x for x in nums]
# print(squared_nums)

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# # sum_nums = [x + y for x, y in zip(nums1, nums2)]
# # print(sum_nums)

# def is_positive(x):
#     return x>0
# num =[ -2,-1,0,1,2]
# positive_nums = list(filter(is_positive, num))
# print(positive_nums)

# some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

# new_str = "".join(list(filter(lambda x: x.islower(), some_str)))
# print(new_str)

# nums = [1,2,3,4,False]
# result = all(nums)
# print(result)
# nums = [1,2,3,4,False]
# result = any(nums)
# print(result)

# words =["Hello", "World", "Python"]
# case1=all(word.istitle() for word in words)
# print(case1)

# def add(a, b):
#     return a + b
# print(add(1,23))

# class MyClass:
#     def __init__(self, value):
#         self.instance_field = value  # Поле класу

# obj1 = MyClass(5)
# obj2 = MyClass(10)

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def say_name(self) -> None:
#         print(f'Hi! I am {self.name} and I am {self.age} years old.')

#     def set_age(self, age: int) -> None:
#         self.age = age

# bob = Person('Boris', 34)

# bob.say_name()
# bob.set_age(25)
# bob.say_name()

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active

#     def greeting(self):
#         return f"Hi {self.name}"

# p = Person("Boris", 34, True)
# print(p.name, p.age, p._is_active)
# print(p.greeting())

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active
#         self._is_admin = is_admin

#     def greeting(self):
#         return f"Hi {self.name}"

#     def is_active(self):
#         return self._is_active

#     def set_active(self, active: bool):
#         self._is_active = active

# p = Person("Boris", 34, True, False)
# print(p._is_admin)

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# print(D.__mro__)  # Виведе порядок розв'язання методів для класу D


# class Dog:
#     def speak(self) -> str:
# #         return "Woof"

# # class Cat:
# #     def speak(self) -> str:
# #         return "Meow"

# # class Robot:
# #     def speak(self) -> str:
# #         return "Beep boop"

# # def make_it_speak(a):
# #     print(a.speak())

# # dog = Dog()
# # cat = Cat()
# # robot = Robot()

# # make_it_speak(Dog())  # Виведе: Woof
# # make_it_speak(Cat())  # Виведе: Meow
# # make_it_speak(Robot())  # Виведе: Beep boop
# class Dog:
#     species = "Canis familiaris"  # Класове поле (одне на всі об'єкти)

#     def __init__(self, name, age):
#         self.name = name  # Поле екземпляра
#         self.age = age    # Поле екземпляра

# # Класове поле:
# print(Dog.species)  # Output: Canis familiaris

# # Поля екземпляра:
# dog1 = Dog("Buddy", 5)
# dog2 = Dog("Max", 3)

# print(dog1.name, dog1.age)  # Output: Buddy 5
# print(dog2.name, dog2.age)  # Output: Max 3

# class Dog:
#     species = "Canis familiaris"  # Атрибут класу

#     def __init__(self, name, age):
#         self.name = name  # Атрибут екземпляра
#         self.age = age    # Атрибут екземпляра

#     def bark(self):  # Атрибут (метод)
#         print(f"{self.name} says Woof!")

# # Екземпляр об'єкта
# dog = Dog("Buddy", 5)

# # Атрибути
# print(dog.name)      # Атрибут екземпляра (поле)
# print(dog.species)   # Атрибут класу (поле)
# dog.bark()           # Атрибут екземпляра (метод)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, {self.name}!")

# person1=Person("Igor")
# person1.greet()

# from collections import UserDict

# class MyDictionary(UserDict):
#     # Приклад додавання нового методу
#     def add_key(self, key, value):
#         self.data[key] = value

# # Створення екземпляра власного класу
# my_dict = MyDictionary({'a': 1, 'b': 2})
# my_dict.add_key('c', 3)
# print(my_dict)

# from dataclasses import dataclass


# @dataclass
# class Rectangle: 
#     width: int
#     height:int

#     def area(self):
#         return self.width * self.height
# rect1 = Rectangle(5,10)
# rect2 = Rectangle(3,6)
# rect3 = Rectangle (4,8)

# print(f'Площа прямокутного трикутника 1: {rect1.area()}')
# print(f'Площа прямокутного трикутника 2: {rect2.area()}')
# print(f'Площа прямокутного трикутника 3: {rect3.area()}')

# from enum import Enum

# class Day(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7
# today = Day.MONDAY
# print(today)  # Виведе: Day.MONDAY

# if today == Day.MONDAY:
#     print("Сьогодні понеділок.")
# else:
#     print("Сьогодні не понеділок.")


# print(today.name)  
# print(today.value)  

# from enum import Enum, auto

# class OrderStatus(Enum):
#     NEW = auto()
#     PROCESSING = auto()
#     SHIPPED = auto()
#     DELIVERED = auto()

# class Order:
#     def __init__(self, name: str, status: OrderStatus):
#         self.name = name
#         self.status = status

#     def update_status(self, new_status: OrderStatus):
#         self.status = new_status
#         print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

#     def display_status(self):
#         print(f"Статус замовлення '{self.name}': {self.status.name}.")

# order1 = Order("Ноутбук", OrderStatus.NEW)
# order2 = Order("Книга", OrderStatus.NEW)

# order1.display_status()
# order2.display_status()

# order1.update_status(OrderStatus.PROCESSING)
# order2.update_status(OrderStatus.SHIPPED)

# order1.display_status()
# order2.display_status()

# try:
#     # Код, який може викликати виняток
#     result = 10 / 0
# except ZeroDivisionError:
#     # Обробка винятку ділення на нуль
#     print("Ділення на нуль!")
# except Exception as e:
#     # Обробка будь-якого іншого винятку
#     print(f"Виникла помилка: {e}")
# else:
#     # Виконується, якщо виняток не був викликаний
#     print("Все пройшло успішно!")
# finally:
#     # Виконується завжди, незалежно від того, був виняток чи ні
#     print("Блок finally завжди виконується.")

# class Heart:
#     def __init__(self):
#         self.status = "Beating"
#     def beat(self):
#         print("Heart is beating...")
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.heart = Heart()  # Композиція: Людина володіє серцем
#     def live(self):
#         print(f"{self.name} is alive!")
#         self.heart.beat()
# person = Person("Alice")
# person.live()
# del person  # Серце також перестає існувати (немає посилань на нього)

# class Heart:
#     def __init__(self):
#         self.status = "Beating"
#     def beat(self):
#         print("Heart is beating...")
# class Person:
#     def __init__(self, name, heart):
#         self.name = name
#         self.heart = heart  # Агрегація: Людина використовує серце
#     def live(self):
#         print(f"{self.name} is alive!")
#         self.heart.beat()
# heart = Heart() # Створюємо серце окремо
# person = Person("Bob", heart) # Створюємо людину, передаючи їй серце
# person.live()
# del person  # Серце все ще існує
# heart.beat()  # Output: Heart is beating...

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point(x={self.x}, y={self.y})"

# point = Point(2, 3)
# print(repr(point))  # Виводить: Point(x=2, y=3)

# class Human:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

 
    
#     def __repr__(self):
#         return f"Human({self.name}, {self.age})"
    
#     def __str__(self):
#         return f"Human named {self.name} who is {self.age} years old"

# human = Human("Alice", 30)
# print(human)

# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __add__(self, other):
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)

#     def __sub__(self, other):
#         return ComplexNumber(self.real - other.real, self.imag - other.imag)

#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag
#         imag_part = self.real * other.imag + self.imag * other.real
#         return ComplexNumber(real_part, imag_part)

#     def __str__(self):
#         return f"{self.real} + {self.imag}i"

# if __name__ == "__main__":
#     num1 = ComplexNumber(1, 2)
#     num2 = ComplexNumber(3, 4)
#     print(f"Сума: {num1 + num2}")
#     print(f"Різниця: {num1 - num2}")
#     print(f"Добуток: {num1 * num2}")

# class Multiplier:
#     def __init__(self, factor):
#         self.factor = factor

#     def __call__(self, other):
#         return self.factor / other

# # Створення екземпляра функтора
# double = Multiplier(2)
# triple = Multiplier(3)

# # Виклик функтора
# print(double(5))  # Виведе: 10
# print(triple(3))  # Виведе: 9


# class Multiplier:
#     def __init__(self,factor):
#         self.factor= factor
#     def __call__(self,other):
#         return self.factor * other
    
# double = Multiplier(2)
# triple = Multiplier(3)
# print(double(5))
# print(triple(3))

# class SmartCalculator:
#     def __init__(self, operation='add'):
#         self.operation = operation

#     def __call__(self, a, b):
#         if self.operation == 'add':
#             return a + b
#         elif self.operation == 'subtract':
#             return a - b
#         else:
#             raise ValueError("Невідома операція")

# add = SmartCalculator('add')
# print(add(5, 3))  # 8

# subtract = SmartCalculator('subtract')
# print(subtract(10, 7))  # 3

# class CountDown:
#     def __init__(self, start):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current == 0:
#             raise StopIteration
#         self.current -= 1
#         return self.current

# if __name__ == '__main__':
#     counter = CountDown(5)
#     for count in counter:
#         print(count)

# def my_generator():
#     try:
#         yield "Working"
#     except GeneratorExit:
#         print("Generator is being closed")

# gen = my_generator()
# print(next(gen))  # Отримуємо "Working"
# gen.close()  # Викликаємо закриття генератора

# import pickle

# # Об'єкт для серіалізації
# my_data = {"key": "value", "num": 42}

# # Серіалізація об'єкта в байтовий рядок
# serialized_data = pickle.dumps(my_data)
# # Виведе байтовий рядок
# print(serialized_data)  

# # Десеріалізація об'єкта з байтового рядка
# deserialized_data = pickle.loads(serialized_data)
# # Виведе вихідний об'єкт Python
# print(deserialized_data)

# import pickle

# class Robot:
#     def __init__(self, name, battery_life):
#         self.name = name
#         self.battery_life = battery_life
#         # Цей атрибут ми не збираємось серіалізувати
#         self.is_active = False  

#     def __getstate__(self):
#         state = self.__dict__
#         # Видаляємо is_active з серіалізованого стану
#         del state['is_active']
#         return state

#     def __setstate__(self, state):
#         # Відновлюємо об'єкт при десеріалізації
#         self.__dict__.update(state)
#         # Задаємо значення is_active за замовчуванням
#         self.is_active = False  

# # Створення об'єкта Robot
# robot = Robot("Robo1", 100)

# # Серіалізація об'єкта
# serialized_robot = pickle.dumps(robot)

# # Десеріалізація об'єкта
# deserialized_robot = pickle.loads(serialized_robot)

# print(deserialized_robot.__dict__)

# class Reader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.fhd = open(self.filename, "r", encoding="utf-8")

#     def close(self):
#         self.fhd.close()

#     def read(self):
#         data = self.fhd.read()
#         return data

# if __name__ == "__main__":
#     reader = Reader("data.txt")
#     data = reader.read()
#     print(data)
#     reader.close()

# my_list = [1, 2, 3]

# def square_list(x: list):
#     for i, el in enumerate(x):
#         x[i] = el**2
#     return x

# new_list = square_list(my_list)
# new_list1 = my_list.append(4)
# print(new_list)
# print(my_list)
# import copy

# class MyClass:
#     def __init__(self, value):
#         self.value = value

#     def __copy__(self):
#         print("Викликано __copy__")
#         return MyClass(self.value)

#     def __deepcopy__(self, memo=None):
#         print("Викликано __deepcopy__")
#         return MyClass(copy.deepcopy(self.value, memo))

# # Поверхневе копіювання
# obj = MyClass(5)
# obj_copy = copy.copy(obj)
# obj_copy.value = 10

# # Глибоке копіювання
# obj_deepcopy = copy.deepcopy(obj)
# obj_deepcopy.value = 20
# print(obj.value, obj_copy.value, obj_deepcopy.value)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# header = '|{:^15}|{:^15}|{:^15}|'.format("int","int^2","int^3")
# separator ="-"*len(header)
# body = ""
# for num in numbers:
#     body += '|{:^15}|{:^15}|{:^15}|\n'.format(num,num**2,num**3)
# table= '\n'.join([separator,header,separator, body,separator])
# print(table)

# from datetime import datetime


# def string_to_date(date_string):
#     date_string ="2024.01.01"
#     converted_date=string_to_date(date_string)
#     return datetime(converted_date)    

# def date_to_string(date):
#     date_string=date_to_string(converted_date)
#     print(date_string)

# from datetime import datetime


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()    

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# date_string = "2024.01.01"
# converted_date = string_to_date(date_string)
# print(converted_date)

# date_string = date_to_string(converted_date)
# print(date_string)

# from datetime import datetime


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def prepare_user_list(user_data):
#     prepared_users=[]
#     for user in users:
#         prepared_user= {
#         "name":user["name"],      
#         "birthday":
#         string_to_date(user["birthday"])
#         }
#         prepared_users.append(prepared_user)
#     return prepared_users
        
# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},   
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# prepared_users = prepare_user_list(users)
# print(prepared_users)


# from datetime import datetime, timedelta


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def find_next_weekday(start_date, weekday):
#     days_ahead = (weekday - start_date.weekday()+7) %7  
#     if days_ahead == 0:
#         days_ahead = 7
#     return start_date + timedelta(days=days_ahead)


# start_date= string_to_date("2024.03.26")
# next_monday = find_next_weekday(start_date, 0)
# next_friday = find_next_weekday(start_date, 4)

# print(next_monday)
# print(next_friday)


# from datetime import datetime, date
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")
# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list
# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#     print("Today's date:", today)
#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)
#         if birthday_this_year < today:
#             birthday_this_year = birthday_this_year.replace(year=today.year+1)

#         days_until_birthday = (birthday_this_year - today).days

#         if 0<= days_until_birthday<=days:
#             upcoming_birthdays.append({
#             "name": user["name"],
#             "congratulation_date": date_to_string(birthday_this_year)
#         })
#     return upcoming_birthdays
# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"}
# ]
# prepared_users = prepare_user_list(users)
# print(get_upcoming_birthdays(prepared_users, 7))







# from datetime import datetime, date

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({
#             "name": user["name"],
#             "birthday": string_to_date(user["birthday"])
#         })
#     return prepared_list

# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     # Override today's date for testing
#     today = date(2024, 3, 27)  # Set today to 2024-03-27 for testing purposes
#     print("Today's date (for testing):", today)  # Debug: Print today's date

#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)

#         if birthday_this_year < today:
#             birthday_this_year = birthday_this_year.replace(year=today.year + 1)

#         days_until_birthday = (birthday_this_year - today).days

#         # Debug outputs
#         print(f"User: {user['name']}, Birthday: {birthday_this_year}, Days Until: {days_until_birthday}")

#         if 0 <= days_until_birthday <= days:
#             upcoming_birthdays.append({
#                 "name": user["name"],
#                 "congratulation_date": date_to_string(birthday_this_year)
#             })

#     return upcoming_birthdays

# # Example users list
# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "Steave Jobs", "birthday": "1990.01.27"}
# ]

# # Process users and get upcoming birthdays
# prepared_users = prepare_user_list(users)
# print(get_upcoming_birthdays(prepared_users, 7))




















