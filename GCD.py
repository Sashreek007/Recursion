def GCP(a,b):
    assert a>=0 and int(a)==a,"Enter postive numbers"
    assert b>=0 and int(b)==b,"Enter postive numbers"
    if b==0:
        return a
    else:
        return GCP(b,a%b)
    
print(GCP(48,18))

