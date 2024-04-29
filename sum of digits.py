def sum_digits(n):
    assert n>=0 and int(n)==n,"Should be positive"
    if n == 0:
        return 0
    else:
        return int(n%10) +sum_digits(n//10)

print(sum_digits(-25))