# put your python code here
num_1, num_2 = input(), input()
num_1 = sorted(set(num_1))
num_2 = sorted(set(num_2))
print('YES' if num_1 == num_2 else 'NO')

'''На вход программе подаются две строки, состоящие из цифр. 
Необходимо определить, верно ли, что для записи этих строк были 
использованы одинаковые наборы цифр?'''