import math 


# gets factors, returns a sorted list
def get_factors(to_factor):
    if to_factor == 1:
        return [1]

    my_list = []
    rnd_sqrt =  math.ceil(math.sqrt(to_factor))

    # range excludes last number, so add +1
    for num in range(1, rnd_sqrt + 1):
        if to_factor % num == 0:
            a_factor = to_factor // num
            my_list.append(a_factor)
            my_list.append(num)

    my_list.sort()
    
    # the set only stores unique values
    my_list = list(set(my_list))

    return my_list

def is_prime(factors):
    # prime numbers only have 2 factors
    return len(factors) == 2

def is_perfect_square(factors):
    # perfeect squares have odd numbers of factors.
    return len(factors) % 2 != 0

factors = get_factors(26)

print(factors)
print(is_prime(factors))
print(is_perfect_square(factors))