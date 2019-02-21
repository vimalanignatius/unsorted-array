a[3,6,5,8,9,10,20]
small=a[20]
for i in range(1,len(a)):
    if(a[i]<small):
        small=a[i]
        return small
    
