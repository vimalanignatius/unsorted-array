def less_count(a,x):
    count=0
    for i in a:
        if(i<=x):
            count+=1
    return count
a=[2,3,5,6,7,8,9]
x=input("enter the value")
print(less_count(a,x))