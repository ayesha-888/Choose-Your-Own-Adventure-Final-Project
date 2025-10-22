import random
import time 

# dice
def dice_6():
    six_rolled = random.randint(1, 6)
    return six_rolled

def dice_10():
    ten_rolled = random.randint(1, 10)
    return ten_rolled

def dice_20():
    twenty_rolled = random.randint(1, 20)
    return twenty_rolled

def dice_50():
    fifty_rolled = random.randint(1, 50)
    return fifty_rolled 

# countdown
def countdown(seconds):
    current_time = seconds
    while current_time >= 0:
        print(current_time)
        time.sleep(1)
        current_time -= 1

# start
def startAdventure():
    print("Welcome to Bikini Bottom!")
    print("Today, you will live the life of SpongeBob Squarepants. \nYour goal is to protect the Krabby Patty secret formula from Plankton. Good luck!")
    start = input("Type 'START' to begin your adventure!: ").strip().lower()
    if start == "start":
        choice_1()
    else:
        print("Invalid input.")
        startAdventure()

# choice 1
def choice_1():
    print("\nSpongeBob arrives at the Krusty Krab and notices the front door is already open... \nThis causes some suspicion, what should he do?:")
    print("A) Go inside cautiously")
    print("B) Run away from the Krusty Krab")
    choice = input("Enter A or B: ").strip().upper()

    if choice == "A":
        print("\nSpongeBob cautiously steps inside and suddenly slips on something wet...")
        choice_2()
    elif choice == "B":
        print("\nSpongebob immediately turns around and runs away from the Krusty Krab, without going inside..")
        print("Later in the day, you find out the formula was stolen... and you weren't there to protect it!")
        lost()
    else:
        print("Invalid input.")
        choice_1()

# choice 2
def choice_2():
    print("\nSpongebob discovers he slipped in what feels like slime! He follows the trail and notices it leads into the kitchen. \nDoes he:")
    print("A) Call Mr. Krabs immediately")
    print("B) Go clean up the slime")
    choice = input("Enter A or B: ").strip().upper()

    if choice == "A":
        print("\nMr. Krabs tells him to wait outside the Krusty Krab for him and everything will be fine.")
        choice_3()
    elif choice == "B":
        print("\nSpongebob gets a bucket and mop to clean the slime while Mr. Krabs arrives.")
        choice_3()
    else:
        print("Invalid input.")
        choice_2()

# choice 3
def choice_3():
    print("Mr. Krabs arrives and tells Spongebob they should follow the trail together. They walk along the remaining slime and it leads them into the kitchen...")
    print("\nRolling the dice to see if following the slime trail leads to something helpful...")
    countdown(3)
    if dice_10() > 6:
        print("\nThey hear munching sounds and find Gary eating Krabby Patties!")
        choice_4()
    else:
        print("\nThe trail disappears into a vent. Mr. Krabs dismisses the trail for some water from a broken pipe and walks away.")
        print("Turns out, the trail was actually slime and it was from Gary.. \nWho had Plankton and the secret formula in his shell unknowingly!")
        lost()

# choice 4
def choice_4():
    print("\nMr. Krabs and SpongeBob look at Gary suspiciously.")
    print("Gary meows and starts sliding towards the back door of the Krusty Krab...")
    print("Do they:")
    print("A) Get back to setting up the kitchen")
    print("B) Follow Gary")
    choice = input("Enter A or B: ").strip().upper()

    if choice == "A":
        print("\nThey ignore Gary. While SpongeBob flips patties, Mr. Krabs yells 'PLANKTON!' from his office...")
        print("Spongebob runs to his office and sees the safe is open... but where's the formula?")
        lost()
    elif choice == "B":
        print("\nGary leads them to the back door, where the door is cracked open...")
        print("Inside, they find a strange metal part... it looks like a piece of Karen!")
        choice_5()
    else:
        print("Invalid input.")
        choice_4()

# choice 5
def choice_5():
    print("\nSpongebob and Mr. Krabs examine the smooth metal piece...")
    print("Do they:")
    print("A) Ask Gary if he saw anything")
    print("B) Search the Krusty Krab for more clues")
    choice = input("Enter A or B: ").strip().upper()

    if choice == "A":
        print("\nGary meows seven times... SpongeBob translates, he says 'Karen was here and took the formula!!!'")
        print("They have to catch them before it’s too late! \nThey begin to search the kitchen near where the metal piece was..")
        choice_6()
    elif choice == "B":
        print("\nThey split up to search the building...")
        print("Rolling a dice to see if they find anything useful...")
        countdown(3)
        if dice_20() > 10:
            print("Mr. Krabs finds a tiny footprint leading to the freezer. Suspicious...")
            choice_6()
        else:
            print("They waste time searching and miss their chance to catch Plankton.")
            lost()
    else:
        print("Invalid input.")
        choice_5()

# choice 6 (dice)
def choice_6():
    print("\nSpongebob and Mr. Krabs approach the freezer door and notice it’s slightly open.")
    print("SpongeBob wants to check it out. Mr. Krabs is hesitant and wants to hold the door open with a spatula.")
    print("Do they:")
    print("A) Enter the freezer to investigate")
    print("B) Grab a spatula to keep the door open first")
    choice = input("Enter A or B: ").strip().upper()

    if choice == "A":
        print("\nThey step inside and the door slams shut behind them... they're locked in!")
        choice_7()
    elif choice == "B":
        print("\nThey wedge a spatula in the doorway and enter cautiously...")
        print("But a strong gust of wind from the vent knocks it loose and the door locks behind them...")
        choice_7()
    else:
        print("Invalid input.")
        choice_6()

# choice 7 (loop)
def choice_7():
    print("\nSpongeBob and Mr. Krabs are stuck in the freezer!")
    print("They need to escape before the formula is stolen!")
    print("Do they:")
    print("A) Try stacking frozen patties to reach the air vent")
    print("B) Start throwing frozen Krabby Patties at the window to break it")
    choice = input("Enter A or B: ").strip().upper()

    if choice == "A":
        print("\nThey try to stack patties and climb toward the vent... but it falls down!")
        print("Mr. Krabs boosts Spongebob up to the vent and he squishes into it")
        print("He crawls through the vents and ends up at one where he has a view of Mr. Krabs office")
        print("Spongebob watches as Plankton and Karen unlock the safe and zoom out of the office. \nSpongebob shouts at them to stop, banging on the vent..")
        lost() 
    elif choice == "B":
        print("\nThey start grabbing the coldest patties they can find...")
        choice_8()
    else:
        print("Invalid input.")
        choice_7()

# choice 8 (loop)
def choice_8():
    print("\nTrying to smash open the lock with Krabby Patties...")
    for attempt in range(3):
        print(f"Attempt {attempt + 1}: Throwing a patty!")
        if dice_50() > 30:
            print("You broke the door open!")
            choice_9()
            break
        else:
            print("The door held. Try again...")
    else:
        print("Too many tries! You're stuck!")
        print("You take too long to escape the freezer, the secret formula is gone!")
        lost()

# choice 9
def choice_9():
    print("Mr. Krabs and Spongebob push the door open and rush into Mr. Krabs office. \nThankfully, the safe seems untouched")
    print("\nMr. Krabs tells Spongebob to open the safe, while he searches the front of the Krusty Krab for a sign Plankton was here. \nBut Spongebob doesn't know the code...")
    correct_code = "321"
    attempts = 0
    code_cracked = False
    while attempts < 3:
        guess = input("Guess the 3-digit code: ")
        if guess == correct_code:
            print("The safe unlocks!")
            code_cracked = True
            break
        else:
            print("Incorrect code.")
            attempts += 1
    if not code_cracked:
        print("You failed to open the safe.")
        print("As you try to crack the code, Plankton sneaks out from behind the grill and escapes through the back door with the formula in hand..")
        lost()
        return
    choice_10()

# choice 10
def choice_10():
    print("\nInside the safe is a vault with the sign: 'SAFE WILL DESTRUCT IF TURNED THE WRONG WAY'")
    print("SpongeBob takes a deep breath. The handle can turn either left or right.")
    print("Does he:")
    print("A) Turn the handle left")
    print("B) Turn the handle right")
    choice = input("Enter A or B: ").strip().upper()

    if choice == "A" or choice == "B":
        print("\nSpongeBob slowly turns the handle...")
        print("Rolling a dice to see what happens...")
        countdown(3)
        roll = dice_6()
        if roll >= 4:
            print("CLICK! The vault unlocks... inside is the Krabby Patty secret formula!")
            win()
        else:
            print("He hears a ticking sound... Spongebob braces for cover and the vault door swings open slowly... \nBut it's empty inside.. Plankton must have gotten to it before you!")
            lost()
    else:
        print("Invalid input.")
        choice_10()

# endings
def lost():
    print("\nYou did not fulfill your duties as a loyal Krusty Krab worker! \nThe secret formula has been stolen by Plankton and it's all your fault! \nYOU'RE FIRED!")
def win():
    print("\nCongratulations! You saved the Krusty Krab! \nThe people of Bikini Bottom lift you up through the city and chant 'SPONGEBOB!' until you reach the Mayor's office and he places a bejeweled crown on your head")
    print("\nYou hear your boat alarm in the distance and open your eyes, it was all just a dream!")
    print("Oh well! Time to go to the Krusty Krab!")

startAdventure()