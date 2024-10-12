
numbers = [1, 2, 3, 4, 5]
print("Список :", numbers)

# Проверяем, что список не пустой
if numbers:
    # Сдвигаем элементы вправо
    last_element = numbers[-1]  # Запоминаем последний элемент
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]  # Сдвигаем элементы
    numbers[0] = last_element  # Ставим последний элемент на первое место


print("Список после сдвига вправо:", numbers)

