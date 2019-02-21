def vcount(a,x):
    count=0
    #while(a[count:]):
        #count+=1
    for i in a:
        if(i==x):
            count+=1
            if(count>1):
                return True
    return False
a=[2,3,4,5,5,6]
x=input("enter the value")
print(vcount(a,x))