a=[]
b=[]
def two_list(a,b):
    for i in range(0,5):
        #print(input("enter the value of x",x))
        x=input("enter the value x:")
        a.append(x)
    for j in range(0,5):
        #print(input("enter the value of y",y))
        y=input("enter the value y:")
        b.append(y)
    if(len(a)==len(b)):
            return True
    return False
print(two_list(a,b))



