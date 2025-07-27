from operator import itemgetter
from pprint import pprint

# Объявляем функцию

def my_func():
    print("Мы вызвали функцию!")

my_func()

# Функция с позиционными аргументами

def sum_numbers(a: int, b: int):
    print(a + b)

sum_numbers(10, 15)
sum_numbers(20, 30)
sum_numbers(-8912479812674981274, 1)

sum_numbers("abc", "def")

# Функция с именованными аргументами

sum_numbers(a=10, b=15)

sum_numbers(b=10, a=15)

# Функция с аргументами по умолчанию

def multiply(n, mult: int = 2):
    print(n * mult)

multiply(10)
multiply(10, mult=5)

print(1, 2, 3, 4, 5, sep=" | ")

# Возвращаем значение


def sum(a: int, b: int):
    return a + b


n = sum(10, 15)
# print(n)

# Возвращаем несколько значений

def return_tuple():
    return 1, 2, 3

t = return_tuple()
print(t)
t1, t2, t3 = return_tuple()
print(t1, t2, t3)

# t1, t2 = return_tuple()
# print(t1, t2)

t1, *t2 = return_tuple()
print(t1, t2)

t1, t2, *t3 = return_tuple()
print(t1, t2, t3)

t1, _, _ = return_tuple()
print(t1)

t1, *_ = return_tuple()
print(t1)

# Переменное количество аргументов на примере print

def custom_print(*args):
    # for arg in args:
    #     print(arg)

    print(args)
    print(*args)


custom_print(1, 2, 3, 4, 5)

# Переменное кол-во именованных аргументов

def custom_named_print(*args, **kwargs):
    print(args, kwargs)
    print(*args, **kwargs)

custom_named_print(1, 2, 3, 4, 5, end="!\n", sep=" | ")

# Область видимости переменных

v = 123

def my_awesome_func():
    v = 456
    print(v)

print(v)
my_awesome_func()
print(v)

# Функция - тоже объект

p = print

p(1, 2, 3, 4, 5)

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]

def get_age(user):
    return user["age"]

# users.sort(key=get_age)

# users.sort(key=lambda user: user["age"])

users.sort(key=itemgetter("age"))

pprint(users)
