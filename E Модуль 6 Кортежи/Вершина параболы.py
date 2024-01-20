a, b, c, = int(input()), int(input()), int(input())
x = -b/(2 * a)
y = a * (x)**2 + b * x+c

koordinate = (round(x, 1), round(y, 1))
print(koordinate)
