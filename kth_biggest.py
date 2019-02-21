def kthbig(a):
    a.sort()
    k=input("enter the number")
    return a[-k]

a=[3,4,5,6,7,9]
print(kthbig(a))