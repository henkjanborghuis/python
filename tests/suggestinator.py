def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("Too short")
    return product_idea + "inator"

try:
    product_idea = input("What is your product idea?     ")
    my_idea = suggest(product_idea)
except ValueError as err:
    print("{}".format(err))
else:    
    print(my_idea)