import math 


# functions go here


#Put series of symbols at sart and end of text
def statement_generator(text, decoration):

    #make string with 5 characters
    ends = decoration * 5

    #add decoration to sart of the statement
    statement ="{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print("Please choose a factor that is in betwen 1 and 200 ")
    print()
    print("This program assumes that factors are whole numbers .")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return

#checks input is a number more than zero
def num_check(question, low, high):
    valid = False
    while not valid:
        
        error = f"please enter a factor that is more than {low} and less or equal to {high}"
        error2= "please enter a factor that does not have decimal part / enter a number"
                                                                         
        try:
        
            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero
            if response >= low and response <= high:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error2)

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

# Main routine goes here

#Heading
statement_generator("Factors Calculator", "-")

#Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time =="":
    instructions()

# Loop to alow multiple calculations
keep_going = ""
while keep_going == "":
   

    comment = ""

    # ask user for number to be factored..
    var_to_factor = num_check("Number? ", 1, 200)
    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor) 
    else:
        factor_list = ""
        comment = "One is special, it is UNITY (only has one factor)"
    
    # comments for squares/ primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
    
    # outputs factors and comment

    # Generate heading
    if var_to_factor == 1:
        heading = "One is special.."

    else:
        heading = "Factors of {}".format(var_to_factor)
    
    # utput factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()

print()
print("Thank you for using the factors calculator")
    