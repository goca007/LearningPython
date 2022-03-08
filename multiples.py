"""
multiples = []
for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        multiples.append(num)

print(sum(multiples))
"""

print(sum(num for num in range(1000) if num % 3 == 0 or num % 5 == 0))


