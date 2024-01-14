n = int(input())
A, numbers_1, numbers_2, numbers_3, numbers_4, numbers_5 = [],[],[],[],[],[]
total, total_2, total_3 = 0,0,0,
flag_1, flag_2, flag_3, flag_4 = True, True, True, True

# создаем матрицу А, путем построчного ввода с клавиатуры
for i in range(n):
    temp = [int(num) for num in input().split()]
    A.append(temp)
  
# код для создания списка чисел от 1 до n
for i in range(1, n**2+1):
    numbers_1.append(i)
  
# код для создания списка чисел матрицы A
for i in range(n):
    numbers_3.append([sum(A[i])]) 
    for j in range(n):
        numbers_2.append(A[i][j])
        if i == j:
            numbers_5.append(A[i][j])
# код сортировки списка 2 и сравниваем со списком 1
numbers_2.sort()
if numbers_1 == numbers_2:
    flag_1 = True
else:
    flag_1 = False
# код для проверки одинаковых сумм в строках
for i in numbers_3:
    for j in i:
        if j == sum(A[0]):
            total +=1
            if total == len(A):
                flag_2 = True
            else:
                flag_2 = False
              
# Код на сумму столбцов, далее анологично предыдущий код
numbers_4 = [sum(row[i] for row in A) for i in range(len(A[0]))]
for i in range(len(numbers_4)):
    for j in range(len(numbers_4)):
        if j == sum(A[0]):
            total_3 +=1
            if total == len(A):
                flag_3 = True
            else:
                flag_3 = False
              
# Это чтобы проверить сумму по главной диагонали
if sum(numbers_5) == sum(A[0]):
    flag_4 = True
else:
    flag_4 = False
        
if (flag_1 and flag_2 and flag_3 and flag_4) == True:
    print('YES')
else:
    print('NO')
