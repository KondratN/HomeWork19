import random
boolCount = True
while boolCount:
    try:
        count_value = int(input("Введите число: "))
        if count_value < 0:
            print("Вы ввели отрицательное число, список не может быть отрицательным!")
            continue
        elif count_value == 0:
            print("Вы ввели 0, список не может быть нулевым!")
            continue
        boolCount = False
    except ValueError:
        print("Вы вводите не число!")
list1 = []
count = 0
while count < count_value:
    try:
        list_item = int(input(f"Введи число под индексом {count}: "))
        list1.append(list_item)
        count += 1
    except ValueError:
        print("Вы вводите не число!")
        print("Попробуйте еще раз!")
print(list1)


def bubble_sort(list1):
    boolbubble = True
    while boolbubble:
        boolbubble = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                boolbubble = True


bubble_sort(list1)
print(list1)