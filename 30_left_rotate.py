def left_rotate(a):
    r=a.pop(0)
    a.append(r)
    return a
a=[4,5,6,7,8]
print(left_rotate(a))