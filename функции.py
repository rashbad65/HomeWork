def get_matrix(n, m, value):
    # Создаем пустой список для хранения всех строк матрицы
    matrix = []

    # Первый (внешний) цикл для создания строк
    for _ in range(n):
        # Создаем пустой список для текущей строки
        row = []

        # Второй (внутренний) цикл для заполнения строки значениями
        for _ in range(m):
            row.append(value)

        # Добавляем заполненную строку в матрицу
        matrix.append(row)

    # Возвращаем матрицу как результат работы функции
    return matrix


# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов на экран
print(result1)
print(result2)
print(result3)