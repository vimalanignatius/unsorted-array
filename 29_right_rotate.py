def right_rotate(a):
    r=a.pop(-2)
    a.insert(0,r)
    return a
a=[2,3,4,5,6]
print(right_rotate(a))