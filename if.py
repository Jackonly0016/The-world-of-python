total = 19 + 9.99 + 13.97 + 20 + 15.97 + 9.97 + 10 * 2
party = 8
print("Receipt for your meal")

if party >= 8:
    total = total + total * .2
    print("We've added the tip automatically, since your party was eight or larger.")
print("Total: ",total)
print("Thank you for dining with us today!")

