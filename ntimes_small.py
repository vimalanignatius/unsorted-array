def nsmall(a):
    small=a[0]
    for i in a:
        if(i<small):
            small=i
        return small

def xsmall(a):
    count=0
    x=nsmall(a)
    for i in a:
        if(i==x):
            count+=1
    return count

a=[2,4,5,6,2,2,2]
print(xsmall(a))
