TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 5
retry = 1
def calculate_price(desired_number_of_tickets):
    return (desired_number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining > 0:
    while retry == 1:
        print("There are {} tickets remaining.".format(tickets_remaining))
        username = input("What's your name, stranger?   ")
        retry += 1
    else:
        try:
            desired_number_of_tickets = input("How many tickets would you like {}?   ".format(username))
            desired_number_of_tickets = int(desired_number_of_tickets)
        except ValueError as err:
            print("That is not a valid selection. Enter a (whole) number")
        else:
            try:
                if desired_number_of_tickets < 1:
                    raise ValueError("The number of tickets has to be greater than 0")
                if desired_number_of_tickets > tickets_remaining:
                    raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
            except ValueError as err:
                print("That is not a valid selection. {}".format(err))
            else:
                total_price = calculate_price(desired_number_of_tickets)
                print("{}, the total price is € {}".format(username, total_price))
                proceed = input("Do you want to proceed with your purchase? Y/N    ")
                if (proceed.upper() == "Y" or proceed.upper() == "YES"):
                    print("You've bought {} tickets".format(desired_number_of_tickets))
                    tickets_remaining -= desired_number_of_tickets
                    retry = 1
                else:
                    print("Thank you {} for looking into this.".format(username))
                    retry = 1
else:
    print("There are no tickets left!")
