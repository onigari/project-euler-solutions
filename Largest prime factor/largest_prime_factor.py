n = 600851475143
from math import sqrt

def is_prime(n) : 
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i += 6
    return True

factors = [i for i in range(1, int(sqrt(n))) if n%i==0]

prime_factors = [i for i in factors if is_prime(i)]

print(max(prime_factors))