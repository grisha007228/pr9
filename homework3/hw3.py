# Инициализация пустого списка
numbers = []

# Ввод чисел до тех пор, пока не введено слово 'end'
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break
    
    # Проверяем, является ли ввод числом
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        number = int(user_input)
        numbers.append(number)
    else:
        print("Пожалуйста, введите корректное целое число.")

# Выводим только нечетные элементы списка
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Нечетные элементы списка:", odd_numbers)
