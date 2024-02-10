def long_word_in_text():
    text=input("Введіть текст")
    words=text.split(" ")
    long_word=max(words, key=len)
    print("Найдовше слово в тексті - ", long_word)
long_word_in_text()