import math 


# gets factors, returns a sorted list
def get_factors(to_factor):
    if to_factor == 1:
        return [1]

    my_list = []

    max_factor = round(math.sqrt(to_factor))

    for item in range(1, max_factor + 1):
        my_list.append(item)

    return my_list

3
    


print(get_factors(1))
print(get_factors(12))
print(get_factors(24))

