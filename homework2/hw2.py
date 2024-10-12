

import math

# Ввод чисел a и b
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

# Определяем границы
start = math.ceil(min(a, b))
end = math.floor(max(a, b))

# Создаем список квадратов целых чисел между a и b, исключая границы
squares = [i**2 for i in range(start + 1, end)]

# Выводим результат
print("Квадраты целых чисел между", a, "и", b, ":", squares)
