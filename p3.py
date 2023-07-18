from random import randint

size = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
a = randint(LOWER_LIMIT, UPPER_LIMIT)
for i in range(0, size):
    b = int(input("Введите число: "))
    if a == b:
        print("Вы угадали")
        break
    if a < b:
        print("Загаданное число меньше " + str(b))
    if a > b:
        print("Загадонное число больше " + str(b))
    if(i != size - 1):
        print("Попробуйте ещё")
    else:
        print("Вы исчерпали все попытки")