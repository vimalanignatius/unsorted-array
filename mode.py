def mode(a):
    count=0
    for i in a:        
        #if(i in d):
            count+=1
            if(i<count):
                return i
    return count
a=[3,3,4,2,2,2,1,1]
print(mode(a))