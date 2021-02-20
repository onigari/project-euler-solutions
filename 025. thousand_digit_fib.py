# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from math import log10

seq = [1,1]
while int(log10(seq[-1])) < 999:
    seq.append(seq[-2]+seq[-1])
    
print(seq.index(seq[-1])+1)