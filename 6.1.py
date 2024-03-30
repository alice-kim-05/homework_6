N, K, M = map(int, input().split())
if N > K:
    Z = N // K
    ost = N - K * Z
    time = (Z * M + M) * 2
    print(time)
elif N <= K:
    time = M * 2
    print(time)
