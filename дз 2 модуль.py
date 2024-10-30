def get_password(n):
    result = ""
    # Перебираем все возможные числа для первого элемента пары
    for i in range(1, 21):
        # Перебираем все возможные числа для второго элемента пары
        for j in range(i, 21):
            # Проверяем, что i не равно j и сумма делится на n без остатка
            if i != j and (i + j) % n == 0:
                result += str(i) + str(j)
    return result

# Вывод паролей для чисел от 3 до 20
for k in range(3, 21):
    print(f"{k} - {get_password(k)}")