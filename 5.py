text=input("Введіть текст")
words=text.split(" ")
capitalize_words = " "
for word in words:
    capitalize_words+=word.capitalize()
print("Всі перші літери слів великі", capitalize_words)