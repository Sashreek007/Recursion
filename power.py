
def power1(n,p):
    assert n>=0 and int(n)==n,"Enter postive numbers"
    assert p>=0 and int(p)==p,"Enter postive numbers"
    if n==0:
        return 0
    elif p==0:
        return 1
    else:
        power= n * power1(n,p-1)
        return power

print(power1(10,10))


