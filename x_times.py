#2.	Given an unsorted integer array A and an integer value X, find if A contains the value X.
def vcount(a,x):
    count=0
    #while(a[count:]):
        #count+=1
    for i in a:
        if(i==x):
            count+=1
            if(count==a):
                return count
    return count
a=[2,3,5,5,5,6,2]
x=input("enter the value")
print(vcount(a,x))