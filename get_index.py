#3.	Given an unsorted integer array A and an integer value X, 
# return the index at which X is located in A or return -1 if it is not found in A.
def count(a,x):
    index=-1
    count=0
    for i in a:
        if(i==x):
            index=count
            break
        count+=1     
    return index
a=[2,3,4,5,7,7]
x=input("enter the value")
print(count(a,x))
         
