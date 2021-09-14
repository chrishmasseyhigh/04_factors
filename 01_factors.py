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
    pass

# Main routine goes here

#Heading
statement_generator("Bit calculator for Integers, Text & Images", "-")

#Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time =="":
    instructions()

# Loop to alow putiple calculations
keep_going = ""
while keep_going == "":
   

    comment = ""

    # ask user for number to be factored..
    var_to_factor = num_check("Number? ")
    if var_to_factor != 1:
      factor_list = get_factors(var_to_factor) 
    else:
        factor_list = ""
        comment = " One is unity, It only has one factor, 1 or itself"
    
    # comments for squares/ primes
    if len(factor_list) == 2:
        comment = " {} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
    