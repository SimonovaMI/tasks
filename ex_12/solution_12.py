import math

earth_radius = 6371.01

latitude_1 = math.radians(float(input('Введите координаты широты первой точки: ')))
longitude_1 = math.radians(float(input('Введите координаты долготы первой точки: ')))
latitude_2 = math.radians(float(input('Введите координаты долготы второй точки: ')))
longitude_2 = math.radians(float(input('Введите координаты долготы второй точки: ')))

distance = earth_radius * math.acos(
    math.sin(latitude_1)*math.sin(latitude_2) +
    math.cos(latitude_1)*math.cos(latitude_2)*math.cos(longitude_1 - longitude_2)
    )

print(f'''Расстояние равно: {distance:.2f} ''')
