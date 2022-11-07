import requests
import bs4

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму: ')) #вводим значение суммы, преобразуем ее в float
per_cent_list = list(per_cent.values()) #получаем список из значений словаря
deposit = list(map(lambda x: x*money/100, per_cent_list)) #умножаем каждый элемент списка на сумму и делим на 100
print('Накопленные средства за год вклада в каждом из банков: ', deposit)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))

#Второй способ
# deposit = []
# for per_cent in per_cent_list:
#     per_cent = per_cent * money / 100
#     deposit.append(per_cent)
# print('Накопленные средства за год вклада в каждом из банков: ', deposit)

