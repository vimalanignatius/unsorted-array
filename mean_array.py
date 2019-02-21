def mean(a):
    count=0
    sum=0
    #temp=0
    for i in a:
        sum+=i
        count+=1
    s=sum/count
    return s
a=[2,2,2]
print(mean(a))
