def nbig(a):
    big=a[0]
    for i in a:
        if(i>big):
            big=i
        return big

def xbig(a):
    count=0
    x=nbig(a)
    for i in a:
        if(i==x):
            count+=1
    return count

a=[8,8,8,2,3,4,4]
print(xbig(a))
