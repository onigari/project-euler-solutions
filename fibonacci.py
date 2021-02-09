# by considering the terms in the Fibonacci sequence(starting with 1, 2) whose values do not exceed four million, find the sum of the even-valued terms.

fib = [1,2]

while fib[-1] < 4000000:
    fib.append(fib[-2]+fib[-1])

fib = fib[:-1]

print(sum([i for i in fib if i%2==0]))
