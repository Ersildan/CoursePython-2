weight, height = float(input()), float(input())
imt = weight / height ** 2

if imt > 25:
    print('Избыточная масса')
elif imt < 18.5:
    print('Недостаточная масса')
else:
    print('Оптимальная масса')
