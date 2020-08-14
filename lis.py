inventory = ['butter',
        'tomato sauce',
        'green beans',
        'chicken',
        'italian herbs',
        'garlic',
        'hamburger',
        'flour',
        'eggs',
        'noodles']

print("Welcome to the Inventory program")
item = input("What item do you want to check? ")
if item in inventory:
    print("Yes, we have that")
else:
    print("No, we don't have that")
