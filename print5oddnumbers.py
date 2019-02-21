def odd(n):
    odd=1
    count=0
    oddnumber=[]
    while(count<n):
        if(odd%2==1):
            oddnumber.append(odd)
            count=len(oddnumber)
        odd+=1
    if(n<0):
        return" no odd"
    return oddnumber
print(odd(5))