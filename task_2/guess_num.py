from random import randrange

num = randrange(1,101)
step = 1

print("Угадайте число от 1 до 100")
user_num = int(input("Введите число: "))

while user_num != num:
    if user_num < num:
        print("Число должно быть больше(")
    elif user_num > num:
        print("Число должно быть меньше(")

    user_num = int(input("Введите число снова: "))
    step = step + 1

print("Вы угадали число - ", num, " За", step, "шагов""\nПоздравляю! Это конец)")
