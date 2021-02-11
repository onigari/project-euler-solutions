from itertools import count

def prime_sequence():
    yield 2; yield 3; yield 5; yield 7;
    sieve = {}
    ps = prime_sequence()
    p = next(ps) and next(ps)
    q = p*p
    for c in count(9,2):
        if c in sieve:
            s = sieve.pop(c)
        elif c < q:  
             yield c
             continue              
        else:
            s=count(q+2*p,2*p)
            p=next(ps)
            q=p*p
        for m in s:
            if m not in sieve:
                break
        sieve[m] = s
        
def first_n_primes(n):
    inf_primes = prime_sequence()
    i, primes = 0, []
    while i < n:
        primes.append(next(inf_primes))
        i += 1
    return primes
    
print(first_n_primes(10001))