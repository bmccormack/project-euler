#Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0

for i in range(1,1000):
    sum += i if 0 in [i % 3, i % 5] else 0
    
print sum