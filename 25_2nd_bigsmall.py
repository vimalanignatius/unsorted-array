def find_len(a): 
    length = len(a) 
    a.sort() 
    print("Largest element is:", a[length-1]) 
    print("Smallest element is:", a[0]) 
    print("Second Largest element is:", a[length-2]) 
    print("Second Smallest element is:", a[1])
a=[12, 45, 2, 41, 31, 10, 8, 6, 4] 
print a
print( find_len(a) )