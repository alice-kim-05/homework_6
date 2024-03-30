M = int(input())
K = M // 7
ost_K = (M - K * 7) + 7
L = M // 5
ost_L = (M - L * 5) + 5
if ost_L == 7 or M % 7 == 0 or ost_K == 5 or K % 5 == 0:
    print('Да')
else:
    print('Нет')