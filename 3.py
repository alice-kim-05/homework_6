n, m = map(int, input().split('х'))
k = int(input())
if k < n * m:
    if k % n == 0 or k % m == 0:
        print('успешно')
    else:
        print('неосуществимо')
else:
    print('неосуществимо')
