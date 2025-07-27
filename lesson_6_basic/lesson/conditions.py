# Boolean - 3 состояния

b = bool

t = True
f = False
n = None

# if/elif/else

if True:
    print("Я выполняюсь!")

if False:
    print("Я никогда не выполнюсь")


code = 400

if 200 <= code < 400:
    print()
    print("Проверка пройдена, хороший ответ!")
elif 400 <= code < 600:
    print("Плохой код ответа")
    print()
    print()
else:
    print("Какой-то странный код")


# Пустые объекты - false

user_list = []

if user_list == []:
    pass

if user_list:
    pass


items_count = 0

if items_count:
    pass


if "abc" == "":
    pass

if "abc":
    pass

print(bool(100))
print(bool(-100))
print(bool(0))


print(bool("abc"))
print(bool(""))

print(bool([]))
print(bool([1, 2, 3]))
print(bool([False]))
print(bool([[]]))