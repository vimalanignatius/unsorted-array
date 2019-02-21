def small(a):
    small=a[0]
    for i in a:
        if(i<small):
            small=i
    return small
            
a=[7,1,4,5]
print(small(a))