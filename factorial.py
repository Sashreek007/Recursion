def factorial(n):
    assert n>=0 and int(n)==n,'The number should be a positive integer'
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3.0))