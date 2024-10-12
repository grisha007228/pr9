# Пример списка чисел
numbers = [1, 10, 5, 6, 18, -1, 500, 6]

# Выводим элементы, которые больше предыдущего
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]

print("Элементы, которые больше предыдущего:", result)

