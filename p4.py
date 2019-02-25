def is_palindromic_number( original ):
    number = original
    reverse = 0
    r = number % 10
    while number > 0:
        r = number % 10
        reverse = reverse * 10 + r
        number = number // 10
    if original == reverse:
        return True
    else:
        return False

max_p = 999 * 999
min_p = 100 * 100
result = 0

for x in range( max_p, min_p, -1):
    if is_palindromic_number( x ):
        for y in range( 999, 100, -1):
            r = x % y
            if r == 0:
                if y >= 100 and y <= 999 and (x//y)<999:
                    result = x
                    break
    if result > 0:
        break
print (result)