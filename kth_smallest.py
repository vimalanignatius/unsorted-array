

def kthsmall(a):
    a.sort()
    k=input("enter the number")
    return a[k-1]


a=[3,4,5,2,6,7]
print(kthsmall(a))