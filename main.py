import random
list = [random.randint(-5, 20) for i in range(10)]
# Задание 1
# В списке целых, заполненном случайными числами вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.
sum_neg = 0
sum_chet = 0
sum_nechet = 0
print(list)
for i in list:
  if i < 0:
    sum_neg += i
  if i % 2 == 0:
    sum_chet += i
  if i % 2 != 0:
    sum_nechet += i
print('Суммa отрицательных чисел = ',sum_neg)
print('Суммa четных чисел = ',sum_chet)
print('Суммa нечетных чисел = ',sum_nechet)


# Задание 2
# Есть список целых, заполненный случайными числами.
# На основании данных этого массива нужно:
# ■ Создать список целых, содержащий только четные числа из первого списка;
# ■ Создать список целых, содержащий только нечетные числа из первого списка;
# ■ Создать список целых, содержащий только отрицательные числа из первого списка;
# ■ Создать список целых, содержащий только положительные числа из первого списка.
task1 = []
task2 =[]
task3 =[]
task4 = []
for i in list:
  if i % 2 ==0:
    task1.append(i)
  else:
    task2.append(i)
  if i < 0:
    task3.append(i)
  else:
    task4.append(i)
print('только четные числа из первого списка',task1)
print('только нечетные числа из первого списка', task2)
print('только отрицательные числа из первого списка', task3)
print('только положительные числа из первого списка', task4)