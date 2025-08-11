def count_words(text):
    words = text.split()
    return len(words)

text = input("Введите текст: ")
word_count = count_words(text)
print(f"Количество слов: {word_count}")