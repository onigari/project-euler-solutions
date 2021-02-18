from math import sqrt
def hf(n):
    factors = []
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            factors.append(i)
    return [1]+factors

x = 9
triangular = 36      #started at 36 because the question already shows the factors upto 28
while len(hf(triangular)) < 250:
    triangular = x*(x+1)//2
    x += 1
print(triangular)