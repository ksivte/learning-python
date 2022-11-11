import requests
import bs4

while(True): #цикл для возврата в начальную точку после отработки исключения
    tickets = input('Введите количество билетов: ')
    try:
        tickets = int(tickets)
        if tickets <= 0:
            raise ValueError
    except ValueError:
        print('Введено некорректное значение')
    else:
        break

age_list = [] #объявляем список для хранения возрастов
for i in range(tickets):
    age = int(input('Введите возраст владельца билета: '))
    age_list.append(age) #добавляем в список полученные значения
print('Возраст владельцев билетов: ', age_list)

sum = 0
for age in age_list: #цикл подсчёта стоимости билетов, до 18 - бесплатно
    if 18 <= age <= 25: #от 18 до 25 - 990
        sum = sum + 990
    elif age > 25: #от 25 - 1390
        sum = sum + 1390

print('Стоимость заказа: ', sum)

if len(age_list) > 3: #применяем скидку, если количество билетов больше 3
    sum = sum - (sum / 100 * 10)
    print('Итоговая стоимость заказа со скидкой: ', sum)

