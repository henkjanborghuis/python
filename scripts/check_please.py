import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
            raise ValueError("More than 1 is required")
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("What is the number of people?   "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Oh no, not a valide number")
    print("{}".format(err))
else:
    print("Each person should pay € {}".format(amount_due))