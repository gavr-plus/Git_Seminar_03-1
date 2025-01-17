# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.



def create_array(n, mn, mx):
    import random
    array = [random.randint(mn, mx) for _ in range(n)]
    return array


n = int(input('Введите количество элементов первого набора: '))
m = int(input('Введите количество элементов второго набора: '))
listing_1 = create_array(n, 2, 13)
listing_2 = create_array(m, 2, 13)
print(listing_1)
print(listing_2)

set_1 = set(listing_1)
set_2 = set(listing_2)

result = set_1 & set_2
print('Пересечение множеств - ', sorted(result), '\n')
