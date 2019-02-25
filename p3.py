import math

def gdc( x, y ):
    if x == y:
        gdc = x
    else:
        smaller = min(x, y)
        bigger = max(x,y)

        r = bigger % smaller
        gdc = smaller
        
        while r > 0:
            gdc = r
            bigger = smaller
            smaller = r
            r = bigger % smaller
    return gdc

def is_prime ( x ):
    #using Fermat's Theorem as in http://mathforum.org/library/drmath/view/51539.html
    bases = [2, 3, 5, 7]    
    for a in bases:
        if gdc( x, a) > 1:
            return False
        else:
            if (a**(x-1)) % x > 1:
                return False
    if x == 3215031751:
        return False
    else:
        return True


number = 600851475143
largest = 1
for i in range( 2, math.floor( math.sqrt(number) ) ):
    if ( i % 2 != 0 and i % 5 != 0 and i % 3 != 0) or i == 2 or i == 3 or i == 5:
        if number % i == 0:
            factor = number//i
            if is_prime(factor):
                largest = factor
                break
            else:
                if is_prime(i):
                    largest = i
        
print (largest)
    





