price_for_small_bottle = 0.1
price_for_big_bottle = 0.25

small_bottles = int(input('Введите число бутылок меньше или объемом 1 литр: '))
big_bottles = int(input('Введите число бутолок объмом больше 1 л: '))

print('Сколько денег можно получить: %.2f доллара' % (price_for_small_bottle*small_bottles + price_for_big_bottle*big_bottles))
