#1. 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def exe_1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No value'


def exe_1_use():
    print(exe_1((int(input('Enter first number: '))), (int(input('Enter second number: ')))))