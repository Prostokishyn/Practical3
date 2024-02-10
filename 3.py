def factorial():
    number=int(input("Введіть число"))
    num=1
    while number>=1:
        num*=number
        number-=1
    print("Факторіал введеного числа = ", num)
factorial()