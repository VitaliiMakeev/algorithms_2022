"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""

def number_reverse(num, number=''):
    if len(str(num)) == 1:
        number += str(num)
        return f'Перевернутое число: {number}'
    else:
        n = num % 10
        number += str(n)
        k = num // 10
        return number_reverse(k, number)

num = int(input('Введите число: '))
print(number_reverse(num))
# len(str(num)) = 3, count = 0
# num = 123 ---> n = 3, number = '3', count = 1
# len(str(num)) = 2, count = 1
# k = 12 ---> n = 2, number = '32', count = 2
# len(str(num)) = 1, count = 2
# k = 1 ---> n = 1, number = '321', count = 3

