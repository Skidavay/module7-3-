print('Задача 1. Должники')

# В базе банка хранятся данные и должников, и законопослушных граждан. Каждому человеку система присваивает свой номер. У нас есть случайная выборка из десяти номеров. Правда, иногда база глючит и выдаёт номер с отрицательным значением. А ещё по статистике, которую собрал наш «МирПрогБанк», каждый второй пользователь брал кредит и не выплатил его вовремя, то есть является должником.

# Напишите программу, которая при вводе десяти чисел определяет, сколько из них являются одновременно чётными и положительными.


enter = 0
for number in range(10):
    number = int(input('Введите число: '))
    if number % 2 == 0 and number > 0:
        enter += 1
print('Число четных и положительны номеров = ', enter)