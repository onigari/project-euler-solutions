# Which starting number, under one million, produces the longest chain?

def collatz(n):
    sequence = []
    while n > 1:
        sequence.append(n)
        if n%2==0:
            n = n//2
        elif n%2==1:
            n = 3*n + 1
    return sequence+[1]

j, lengths = 14, []
while j<1000000:
    lengths.append(len(collatz(j)))
    j += 1
longest = max(lengths)

i = 999999
while i>14:
    seq = collatz(i)
    if len(seq) == longest:
        print(i)
        break
    i -= 1