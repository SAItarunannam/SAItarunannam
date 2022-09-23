a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
d=int(input("enter d value:"))
if a==b or b==c or c==d or a==c or a==d or b==d:
    print("error")
elif a<b and a<c and a<d:
    print("the value of a is less")
elif b<c and b<d:
    print("the value of b is less")
elif c<d:
    print("the value of c is less")
else: 
    print("the value of d is less")