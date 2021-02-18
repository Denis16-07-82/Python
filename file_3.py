#
# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки
interest=int(input('введите процент числом: '))
if interest==1:
    print(f"{interest} процент\n")
elif interest<5:
    print(f"{interest} процента\n")
elif 5<=interest<=20:
    print(f"{interest} процентов\n")
for interest in range(1,21):
    if interest == 1:
        print(f"{interest} процент")
    elif interest < 5:
        print(f"{interest} процента")
    elif 5 <= interest <= 20:
        print(f"{interest} процентов")
