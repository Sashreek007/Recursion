def recursion(n):
    if n<1:
        print("n is less than 1")
    else:
        recursion(n-1)
        print(n)

def first_method():
    second_method()
    print("I am first method")

def second_method():
    third_method()
    print("I am second method")

def third_method():
    fourth_method()
    print("I am third method")

def fourth_method():
    print("I am fourth method")

recursion(4)
#Follows last in first out(LIFO)

first_method()

def poweroftwo(n):
    if n==0:
        return 1
    else:
        power=poweroftwo(n-1)
        return power*2
print(poweroftwo(3))

