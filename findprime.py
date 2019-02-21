import validate_prime

def primenumbers2(Nu):
    primenumbers=[]
    if (Nu<=1 or Nu==2):
        return "not prime"
    for i in range(2,Nu):
        if validate_prime.isprime(i):
            primenumbers.append(i)
    return primenumbers

print(primenumbers2(20))
