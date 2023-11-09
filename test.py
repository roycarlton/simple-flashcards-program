import os, random

class Card:
    def __init__(self, filename):
        card_file = open(filename, "r")
        data = card_file.read().split("\n")
        card_file.close()
        self.title = data[0]
        self.answer = data[1]

#Prints a text promt to the user and if they respond "Y" or "y" returns True, otherwise False
def yn(text):
    affirmative = ["y", "Y"]
    if input(text) in affirmative:
        return True
    else:
        return False

#Display options for cards sets and asks user to select one
def card_set_selection():
    options = []
    search = os.listdir()
    for item in search:
        if os.path.isdir(item) and item[0] != ".":
            options.append(item)

    if len(options) > 0:
        print("Select a card set by entering its number:\n")
        num = 1
        for set in options:
            print(str(num) + ".\t" + set + "\n")
            num += 1

        while True:
            try:
                selection = int(input("Enter selection: "))
                if selection > 0 and selection <= len(options):
                    print(options[selection-1] + " selected.\n")
                    break
                else:
                    print("Invalid input, please select one of the numbers above.")
            except ValueError:
                print("Invalid input, please try again.")

        return options[selection-1]

    else:
        print("No card sets found, exiting program.")
        exit()

#Loads cards from selected set as Card objects in "cards" list
def load_cards(card_dir):
    cards=[]
    all_files = os.listdir(card_dir)
    for file in all_files:
        temp = Card(str(card_dir) + "/" + file)
        cards.append(temp)
    return len(all_files), cards

#Tests each card in the set
def test(card_no, cards):
    
    #Shuffle cards
    random.shuffle(cards)

    total_correct = 0
    wrong_answers = []

    for card in cards:
        print(card.title)
        input()
        print(card.answer)
        if yn("Were you correct? (y/n) "):
            total_correct += 1
        else:
            wrong_answers.append(card.title)
        print("\n")

    print("You got " + str(total_correct) + "/" + str(card_no))

    if len(wrong_answers) > 0:
        print("\nCards you should work on:\n")
        for title in wrong_answers:
            print(title)
    print()


card_dir = card_set_selection()

card_no, cards = load_cards(card_dir)

running = True

while running:
    test(card_no, cards)
    if not(yn("Test again? (y/n) ")):
        running = False