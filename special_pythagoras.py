# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

triplets = list((a,b) for a in range(1, 376) for b in range(1, 376) if a<b and 1000*a + 1000*b - a*b == 500000)
(a, b) = triplets[0]
c = 1000 - a - b
print(f"a={a}, b={b}, c={c}\nabc={a*b*c}")