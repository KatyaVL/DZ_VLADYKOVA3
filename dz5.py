#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def calc_sum(*nums):
    sum = 0
    symbol = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            symbol = True
    return sum, symbol

general_sum = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop_symbol = calc_sum(*numbers_string)
    general_sum += sum
    print(f'сумма {general_sum}')

    if stop_symbol:
        break