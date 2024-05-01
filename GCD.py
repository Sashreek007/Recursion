def GCP(a,b):
    assert a>=0 and int(a)==a,"Enter postive numbers"
    assert b>=0 and int(b)==b,"Enter postive numbers"
    if b==0:
        return a
    else:
        return GCP(b,a%b)
    
print(GCP(48,18))

for i in range(2000,2500):
    if i%4==0 and i%100!=0:
        print(i,"this is a leap year")
    elif i%400==0:
        print(i,"this is a leap year")
    else:
        print(i,"this is not a leap year")