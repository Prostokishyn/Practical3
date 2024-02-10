def long_word_in_text():
    text=input("Введіть текст")
    words=text.split(" ")
    long_word=len(words)
    print("Кількість слів в тексті - ", long_word)
long_word_in_text()