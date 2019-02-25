seq = [1,2]
sum = 2

x = seq[0] + seq[1]
while x <= 4000000:
    if x%2==0:
        sum += x
    seq[0] = seq[1]
    seq[1] = x
    x = seq[0] + seq[1]

print(sum)