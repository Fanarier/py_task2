import random

def task1():
    # Генерация случайных чисел и запись в файл f
    with open("f.txt", "w") as f:
        numbers = [random.randint(1, 100) for _ in range(20)]
        f.write(" ".join(map(str, numbers)))

    # Чтение из файла f и исключение повторов
    with open("f.txt", "r") as f:
        numbers = list(map(int, f.read().split()))
        unique_numbers = sorted(set(numbers))  # Убираем повторы и сортируем

    # Запись в файл g
    with open("g.txt", "w") as g:
        g.write(" ".join(map(str, unique_numbers)))

    # Вывод содержимого файла g
    with open("g.txt", "r") as g:
        print("Содержимое файла g:", g.read())
