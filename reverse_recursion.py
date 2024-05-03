def reverse(n):
    if len(n)<=1:
        return n
    else:
        return n[-1] + reverse(n[:-1]) 
    