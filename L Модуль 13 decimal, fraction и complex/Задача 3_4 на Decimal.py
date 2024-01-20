from decimal import *

'''Задача 3
Дополните приведенный код, чтобы он вывел сумму
наибольшей и наименьшей цифры Decimal числа.'''

num = Decimal(input())
cyphers = num.as_tuple().digits
print(max(cyphers) + min(cyphers) * (abs(num) >= 1))

'''Задача 4
На вход программе подается Decimal число d. 
Напишите программу, которая вычисляет значение выражения:'''

d = Decimal(input())
print(d.exp() + d.ln() + d.log10() + d.sqrt())
