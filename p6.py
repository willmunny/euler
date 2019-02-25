s_sqares = 0
squares_sum = 0

for x in range(1, 101):
    s_sqares += x**2
    squares_sum += x

print( squares_sum**2 - s_sqares )