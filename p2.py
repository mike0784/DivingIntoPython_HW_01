b = True
while True:
    a = int(input("Введите целое число: "))
    if a >=1 and a < 100000:
        break
    else:
        print("Вы ввели неправильное число\nПопробуйте ещё раз")

        
for i in range(2, int(a / 2)):
    if a%i == 0:
        b = False
        break

if b:
    print("Число " + str(a) + " является простым")
else:
    print("Число " + str(a) + " не является простым")