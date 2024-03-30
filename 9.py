xc_1 = int(input())
yc_1 = int(input())
r_1 = int(input())
xc_2 = int(input())
yc_2 = int(input())
r_2 = int(input())
d = ((xc_2 - xc_1) ** 2 + (yc_2 - yc_1) ** 2) ** 0.5
if d == r_1 + r_2:
    print('Окружности имеют внешнее касание')
elif d > r_1 + r_2:
    print('Окружности лежат одна вне другой, не касаясь')
elif d < abs(r_1 - r_2):
    print('Одна окружность лежит внутри другой, не касаясь')
elif abs(r_1 - r_2) < d < r_1 + r_2:
    print('Окружности пересекаются')
elif d < abs(r_1 - r_2):
    print('Окружности имеют внутреннее касание')
