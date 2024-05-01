def binary1(n):
    if n==0:
        return 0
    else:
        return n%2 +10*binary1(int(n/2))

print(binary1(10))