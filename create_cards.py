import os
from test import card_set_selection
from test import yn

sets_dir = "card_sets"

print("""Would you like to:
1.\tCreate a new card set.
2.\tAdd cards to an existing set.\n
""")

while True:
    try:
        selection = int(input("Enter selection: "))
        if selection > 0 and selection <= 2:
            break
        else:
            print("Invalid input, please select one of the numbers above.")
    except ValueError:
        print("Invalid input, please try again.")


if selection == 1:
    while True:
        try:
            card_dir = input("Enter name for new card set: ")
            card_dir = os.path.join(sets_dir, card_dir)
            os.mkdir(card_dir)
            break
        except OSError:
            print("Card set name must be a valid directory name, please try again.")

else:
    card_dir = card_set_selection()

print("""*************************************************************
Now generating cards for the """+ card_dir +""" set.
Using the same title as an existing card will overwrite it.
*************************************************************\n
""")

while True:
    title = input("Enter card title: ")
    answer = input("Enter card answer: ")
    file = open(os.path.join(card_dir, title+".txt"), "w")
    file.write(title + "\n" + answer)
    file.close()
    if not(yn("Add another card? (y/n) ")):
        break