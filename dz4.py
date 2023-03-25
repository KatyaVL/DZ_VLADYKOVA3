#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    counter = 1
        result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result


print(f'Возведения степени вариантом 1: '
      f'{my_func(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')


print(f'Возведения степени вариантом 2: '
      f'{my_func_2(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')