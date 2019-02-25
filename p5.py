x = 2520

numbers = range(20, 1, -1)

founded = False

while True:
    x += 1
    founded = True
    for i, y in enumerate(numbers):        
        if x % y != 0:
            founded = False
            break
        
    if founded:
        break

print(x)
