a=[]
def perfectsq(a):
    count=0
    for i in range(0,5):
        print(count)
        x=input("enter the value")
        a.append(x)
        for i in range(0,x):
            b=i*i
            if(b==x):
                return b
print(perfectsq(a))