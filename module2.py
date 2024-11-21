def task2():
    # Чтение текста из файла
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Разделение текста на слова и поиск самого длинного
    words = text.split()
    longest_word = max(words, key=len)
    count = words.count(longest_word)

    print(f"Самое длинное слово: {longest_word}")
    print(f"Количество вхождений: {count}")
