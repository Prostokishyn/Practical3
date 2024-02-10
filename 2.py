def exponent():
    number=int(input("Введіть число"))
    expnnt=int(input("Введіть степінь, до якого хочете піднести число"))
    res=1
    for _ in range(expnnt):
        res*=number
    return res
print("Число піднесене до степення", exponent())