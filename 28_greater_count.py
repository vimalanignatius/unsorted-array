def great_count(a,x):
    count=0
    for i in a:
        if(i>=x):
            count+=1
    return count
a=[6,7,8,9,7,4]
x=input("enter the number")
print(great_count(a,x))
