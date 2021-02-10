# Find the sum of all primes below two million

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
    
print(sum([i for i in range(2, 2000000) if is_prime(i)]))