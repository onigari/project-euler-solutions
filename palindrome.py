# Find the largest palindrome made from the product of two 3-digit numbers.

i, j, palindromes = 999, 999, []
while i > 100:
    while j > 100:
        product = i*j
        if str(product) == str(product)[::-1]:
            palindromes.append(product)
        j -= 1
    i -= 1
    j = 999
    
print(max(palindromes))