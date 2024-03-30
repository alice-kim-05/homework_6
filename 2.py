a, b = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))
s_1 = a * b
s_2 = c * d
s_3 = c * e
s_4 = d * e
if s_1 >= s_2 or s_1 >= s_3 or s_1 >= s_4:
    print('да')
else:
    print('нет')
