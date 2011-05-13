
import math

def generate_primes(lower_bound, upper_bound):
    
    '''
    This function generates primes that occur between the lower_bound and
    upper_bound. It will return a generator expression, and does not consider
    1 or any negative numbers to be prime.
    '''
    
    if lower_bound>=upper_bound:
        return
    
    prime_check_array = [2]

    if lower_bound <= 2:
        
        if upper_bound < 2:

            return
        
        lower_bound = 3
        yield 2
    
    else:
        for possible_prime in range(3,lower_bound):
            prime = True
            for check_prime in prime_check_array:
                if possible_prime % check_prime == 0:
                    prime == False
                    break
            if prime:
                prime_check_array.append(possible_prime)
    

    max_check_prime = math.floor(math.sqrt(upper_bound))
    
    for possible_prime in range(lower_bound, upper_bound+1):
            prime = True
            for check_prime in prime_check_array:
                if possible_prime % check_prime == 0:
                    prime = False
                    break
            if prime:
                if possible_prime <= max_check_prime:
                    prime_check_array.append(possible_prime)
                yield possible_prime

    
if __name__ == '__main__':
    
    #1 to 10 test
    print "Generating primes from 1 to 10"
    for p in generate_primes(1,100):
        print p
        
    #-10 to 2 test
    print "Generating primes from -10 to 2"
    for p in generate_primes(-10,2):
        print p
    
    #-100 to -10 test
    print "Generating primes from -100 to -10"
    for p in generate_primes(-100,-10):
        print p
    
    #1000 to 1100 test
    print "Generating primes from 1000 to 1100"
    for p in generate_primes(1000,1100):
        print p
    
    #invalid input
    print "Generating primes from 100 to -100 (invalid)"
    for p in generate_primes(100,-100):
        print p
