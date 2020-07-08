shopping_list = []

def add_to_list(item):
    shopping_list.append(item)
    print("{} added to the list. There are {} item(s) on the list".format((item), (len(shopping_list))))


def show_help():
    print("What should we take from the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'SHOW' to show the shopping list.
Enter 'HELP' to show this help.
""")

# Define a function named show_list that prints all the item in the list
def show_list():
    print("Here's our list: ")
    for item in shopping_list:
        #print("- {}").format(item)
        print(item)


show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

show_list()
