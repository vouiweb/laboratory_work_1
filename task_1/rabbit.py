a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
if c != a:
    print(abs(1 - a*b**c - a*(b**2 - c**2) + (b - c + a) * (12 + b)/(c-a)))
else:
    print('Переменная c != a')
