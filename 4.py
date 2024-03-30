n = input()
m = int(n[1])
l = n[0]
for i in range (1,8+1,2):
    if m == i:
        if l == 'a' or l == 'c' or l == 'e' or l == 'g':
            print('черный')
        if l == 'b' or l == 'd' or l == 'f' or l == 'h':
            print('белый')
for i in range (2,8+1,2):
    if m == i:
        if l == 'a' or l == 'c' or l == 'e' or l == 'g':
            print('белый')
        if l == 'b' or l == 'd' or l == 'f' or l == 'h':
            print('черный')
