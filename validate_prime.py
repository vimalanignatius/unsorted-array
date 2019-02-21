import math
def isprime(n):
    Flag=True
    if(n==1):
        return False

    if(n<=0):
        return False

    if(n==2):
        return True

    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            flag= False
    return Flag
    