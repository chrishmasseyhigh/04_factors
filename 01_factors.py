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
def num_check(question, low):
    valid = False
    while not valid:
        
        error = "please enter a factor that is more than 1 and less or equal to 200 "
        error2= "please enter a factor that does not have decimal part / enter a number"
                                                                         
        try:
        
            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero
            if response >= low:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error2)

# gets factors, returns a sorted list
def get_factors(to_factor):
    d