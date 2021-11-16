# -*- coding: utf-8 -*-
import os
# можно реализовать ввод данных с клавиатуры, но по заданию не было такого требования
amnt = (12, 15, 0, 3, 2, 4, 10, 0, 0, 0) # количество осадков
temp = (1, -1, -2, -4, -5, -7, -5, -3, 0, 1) # температура
wthr = ('Snow', 'Rain', 'No precipitation') # кортеж имен погоды


def prec(a): #находит погоду по дню
    if amnt[a] > 0 and temp[a] > 0:
        wth = f"Weather is: {wthr[1]}\n" \
              f"Temp: {temp[a]}\n" \
              f"Amount: {amnt[a]}\n"

        print(wth)
    elif amnt[a] > 0 and temp[a] < 0:
        wth = f"Weather is: {wthr[0]}\n" \
              f"Temp: {temp[a]}\n" \
              f"Amount: {amnt[a]}\n"
        print(wth)
    elif amnt[a] <= 0:
        wth = f"Weather is: {wthr[2]}\n" \
              f"Temp: {temp[a]}\n" \
              f"Amount: {amnt[a]}\n"
        print(wth)


def amount(a, b): # находит кол - во дней с опр. погодой
    amnt1 = amnt[a:b]
    temp1 = temp[a:b]
    rain = 0
    snow = 0
    nprc = 0;
    for x, z in zip(amnt1, temp1):
        if x > 0 and z > 0:
            rain += 1
        elif x > 0 and z < 0:
            snow += 1
        elif x == 0:
            nprc += 1
    print(f"Rainy days: {rain}\n"
          f"Snowy days: {snow}\n"
          f"No falls: {nprc}\n")


def menu(): # меню для выбора функций
    os.system('cls')
    print(f"In database i have {len(amnt)} entries about weather\n"
          f"What do you want to see:\n"
          f"1 - Weather in a day\n"
          f"2 - Precipitations for the period\n"
          f"3 - Exit\n")

    x = int(input())

    if x == 1:
        os.system('cls')
        print(f"Which day (0 - {len(amnt) - 1}): ")
        z = int(input())
        if z > 9 or z < 0:
            print("Wrong number!")
            input("Press Enter to continue...")
            menu()
        else:
            prec(z)
            input("Press Enter to continue...")
            menu()
    elif x == 2:
        os.system('cls')
        print(f"What period (form - 'a b'): ")
        tpl = tuple(map(int, input().split()))
        a, b = tpl
        if a > b or a > 9 or a < 0 or b > 9 or b < 0 or (a == 0 and b == 0):
            print("Wrong number!")
            input("Press Enter to continue...")
            menu()
        else:
            amount(a, b)
            input("Press Enter to continue...")
            menu()
    elif x == 3:
        exit(0)


menu()
