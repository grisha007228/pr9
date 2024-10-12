
numbers = [1, 2, 3, 500, 1, -100]
print("список:", numbers)


# Находим индексы минимального и максимального элементов
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

# Меняем местами минимальный и максимальный элементы
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

# Выводим изменённый список

print("Изменённый список:", numbers)
