def big(a):
    count=0
    for i in a:
        count+=1
        if(count>i):
            return count

a=[2,3,4,5,1]
print(big(a))