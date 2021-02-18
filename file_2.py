# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
my_list=[]
my_list_1=[]
my_list_2=[]
for number in range(1,1000):
    if number%2==1:
        my_list.append(number**3)
print(my_list)
sum_odd_nambers=0
sum_odd_nambers_1=0
for odd_number in range(len(my_list)):
    sum_number=0
    for degree_number in range(9):
        my_number=(my_list[odd_number])//(10**(8-degree_number))
        sum_number+=my_number%(10)
    if sum_number%7==0:
        my_list_1.append(my_list[odd_number])
        sum_odd_nambers+=(my_list[odd_number])
for odd_number in range(len(my_list)):
    sum_number = 0
    for degree_number in range(9):
        my_number=(my_list[odd_number]+17)//(10**(8-degree_number))
        sum_number+=my_number%(10)
    if sum_number%7==0:
        my_list_2.append(my_list[odd_number]+17)
        sum_odd_nambers_1+=(my_list[odd_number])
print(my_list_1)
print(sum_odd_nambers)
print(my_list_2)
print(sum_odd_nambers_1)