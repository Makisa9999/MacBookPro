def isPrime(n):

    if n > 1:  
        for i in range(2,n):  
            if (n % i) == 0:  
                return False
 
        return True
    else:  
        return False

print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(4))
print(isPrime(5))
print(isPrime(6))
print(isPrime(7))
print(isPrime(8))
print(isPrime(9))
print(isPrime(10))
print(isPrime(11))