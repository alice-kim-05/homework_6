R = 6.5
a, b = map(int, input().split('x'))
if (a ** 2 + b ** 2) ** 0.5 <= 2 * R:
    print('да')
else:
    print('нет')