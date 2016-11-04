#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89

x, y = 1,2
sum = 0

while y < 4000000:
    sum += y if y % 2 == 0 else 0
    next_y = y+x
    x = y
    y = next_y
    
print sum
    
