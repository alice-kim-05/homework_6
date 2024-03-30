sq_1, sq_2 = map(str, input().split('-'))
let_1 = sq_1[0].upper()
let_2 = sq_2[0].upper()
fig_1 = int(sq_1[1])
fig_2 = int(sq_2[1])
if abs(ord(let_1) - ord(let_2)) == 1 and abs(fig_1 - fig_2) == 2:
    print('верно')
elif abs(ord(let_1) - ord(let_2)) == 2 and abs(fig_1 - fig_2) == 1:
    print('верно')
else:
    print('ошибка')