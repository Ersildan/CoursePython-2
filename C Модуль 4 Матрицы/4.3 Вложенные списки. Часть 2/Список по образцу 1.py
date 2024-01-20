# put your python code here
n = int(input())
my_list = []

for i in range(1, n +1):
    my_list.append(i)
  
my_list = [my_list for _ in range(n)] 

print(*my_list, sep='\n')
