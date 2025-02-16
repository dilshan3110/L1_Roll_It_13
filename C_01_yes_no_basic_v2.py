
# functions go here

def yes_no(question):

    # checks user response to a question is yes / no (y/n), returns 'yes' or 'no'

    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "y":
            return "no"
        else:
            print("please enter yes / no")

# Main Routine

# Testing loop...
while True:
    want_instructions = yes_no("Do you want to see the instructions? ")
    print(f"you chose {want_instructions}"

print("we are done")
