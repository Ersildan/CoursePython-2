def func(num1, num2):
    flag = False
    a = num1 % num2
    if a == 0:
        flag = True
    return flag


num1, num2 = int(input()), int(input())

if func(num1, num2) == True:
    print('делится')
else:
    print('не делится')
