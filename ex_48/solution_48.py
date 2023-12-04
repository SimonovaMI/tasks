import datetime
input_str = input("Введите число и месяц своего рождения в формате число.месяц ")

list = input_str.split('.')

input_date = datetime.date(year=1970, month=int(list[1]), day=int(list[0]))

if datetime.date(year=1970, month=1, day=20) <= input_date <= datetime.date(year=1970, month=2, day=18):
    print('Водолей')
elif datetime.date(year=1970, month=2, day=19) <= input_date <= datetime.date(year=1970, month=3, day=20):
    print('Рыбы')
elif datetime.date(year=1970, month=3, day=21) <= input_date <= datetime.date(year=1970, month=4, day=19):
    print('Овен')
elif datetime.date(year=1970, month=4, day=20) <= input_date <= datetime.date(year=1970, month=5, day=20):
    print('Телец')
elif datetime.date(year=1970, month=5, day=21) <= input_date <= datetime.date(year=1970, month=6, day=20):
    print('Близнецы')
elif datetime.date(year=1970, month=6, day=21) <= input_date <= datetime.date(year=1970, month=7, day=22):
    print('Рак')
elif datetime.date(year=1970, month=7, day=23) <= input_date <= datetime.date(year=1970, month=8, day=22):
    print('Лев')
elif datetime.date(year=1970, month=8, day=23) <= input_date <= datetime.date(year=1970, month=9, day=22):
    print('Дева')
elif datetime.date(year=1970, month=9, day=23) <= input_date <= datetime.date(year=1970, month=10, day=22):
    print('Весы')
elif datetime.date(year=1970, month=10, day=23) <= input_date <= datetime.date(year=1970, month=11, day=21):
    print('Скорпион')
elif datetime.date(year=1970, month=11, day=22) <= input_date <= datetime.date(year=1970, month=12, day=21):
    print('Стрелец')
else:
    print('Козерог')

print('Коммит')






