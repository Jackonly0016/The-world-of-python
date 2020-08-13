#from getpass import getpass
#password = getpass()


breakfast_special = "Texas Omelet"
breakfast_notes = "Contains brisket, horseradish cheddar"
lunch_special = "Greek patty melt"
lunch_notes = "Like the regular one, bue with tzatziki sauce"
dinner_special = "Buffalo steak"
dinner_notes = "Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT."

meal_time = input('Which mealtime do you want? [breakfast, lunch, dinner] ')
print('Specials for {}:'.format(meal_time))

if meal_time == 'breakfast':
    print(breakfast_special)
    print(breakfast_notes)
elif meal_time == 'lunch':
    print(lunch_special)
    print(lunch_notes)
elif meal_time == 'dinner':
    print(dinner_special)
    print(dinner_notes)
else:
    print('Sorry, {}isn\'t valid.'.format(meal_time))
