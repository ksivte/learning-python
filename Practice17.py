import requests
import bs4


while True:  # цикл для возврата в начальную точку после отработки исключения
    seq_numbers = input('Введите последовательность чисел через пробел: ').split()
    seq_numbers = list(seq_numbers)
    if len(seq_numbers) <= 1:  # проверка, что последовательность содержит больше 1 элемента
        print('Введенная последовательность содержит один или меньше элементов')
        continue  # возврат в начало цикла
    try:
        seq_numbers = list(map(int, seq_numbers))  # проверка, что последовательность состоит из чисел
    except ValueError:
        print('Ошибка! Последовательность включает в себя некорректные элементы (не числа)')
    else:
        break
print(str(seq_numbers))

while True:  # цикл для возврата в начальную точку после отработки исключения
    number = input('Введите число: ')
    try:
        number = int(number)  # проверка, что введено число
    except ValueError:
        print('Ошибка! Введено не число')
    else:
        break


def sort_seq(seq_numbers):  # функция сортировки, сортировка пузырьком
    for i in range(len(seq_numbers)):
        for j in range(len(seq_numbers) - i - 1):
            if seq_numbers[j] > seq_numbers[j + 1]:
                seq_numbers[j], seq_numbers[j + 1] = seq_numbers[j + 1], seq_numbers[j]

    print('Отсортированный по возрастанию список: ', seq_numbers)


left = 0
right = len(seq_numbers) - 1
def binary_search(seq_numbers, number, left, right):  # функция бинарного поиска введенного элемента
    if left > right:
        print('Ошибка! Последовательность не отсортирована')
        return

    middle = (right + left) // 2
    if seq_numbers[middle - 1] < number <= seq_numbers[middle]:  # проверка на соответствие условию
        print('Индекс искомого элемента: ', middle - 1)
    elif number < seq_numbers[middle - 1]:
        binary_search(seq_numbers, number, left, middle - 1)
    else:
        binary_search(seq_numbers, number, middle + 1, right)


sort_seq(seq_numbers)  # вызов функции сортировки

if number <= seq_numbers[0] or number >= seq_numbers[len(seq_numbers) - 1]:
    print('Введенное число равно/меньше первого или равно/больше последнего элемента отсортированной последовательности')
    print('Поиск невозможен')
else:
    binary_search(seq_numbers, number, left, right)