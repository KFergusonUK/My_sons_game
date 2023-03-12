answer_A = ["A", "a"]

answer_B = ["B", "b"]

answer_C = ["C", "c"]

help_calls = 0

print("Bens Text Based Adventure Game.")

#This is the start function:


def Start():

    print("You wake up in your bed, everything is quiet, what do you do?")

    print("A. Get up")  #\n is a new line.

    print("B. Stay in bed, you're tired.")

    choice = input("Please enter A, or B: ")

    if choice in answer_A:

        get_up()

    elif choice in answer_B:

        print("\nOK, Have a nice sleep")

        Start()

    else:

        Start()


#Get out of bed (answer a):


def get_up():

    print(
        "\nYou get out of bed. The air feels strange. You feel a warm wind brush past your hair. WAIT!, a wind? Inside?... There is a hole in the wall and also a closed door, do you..."
    )

    print("A. Investigate the hole")

    print("B. Call for help")

    print("C. Open the door")

    choice = input("Please enter A, B or C: ")

    if choice in answer_A:

        inv_h()

    elif choice in answer_B:

        call_help()

    elif choice in answer_C:

        door()


#Investigate the hole:


def inv_h():

    print(
        "\nThe hole appeares to be caused by some kind of monster, but you can't see any outside..."
    )

    get_up()


#Bedroom Help Call:


def call_help():

    print("\nYou call for help. Nothing happens")

    get_up()


#Open the bedroom door:


def door():

    print(
        "\nEverything seems normal outside the bedroom... You leave the bedroom, what do you do next?"
    )

    print("A. Go to the bottom floor")

    print("B. Go to the top floor")

    print("C. Check the other rooms")

    choice = input("Please enter A, B or C: ")

    if choice in answer_A:

        bottom_floor()

    elif choice in answer_B:

        top_floor()

    elif choice in answer_C:

        check_rooms()


#Bottom floor:


def bottom_floor():

    print(
        "\nEverything seems fine, but the garden doesn't... You go in the garden and find a clone of yourself... ...but evil! What do you attack them with?"
    )

    print("A. A sword")

    print("B. A bow")

    print("C. A ball made of grass")

    choice = input("Please enter A, B or C: ")

    if choice in answer_A:

        sword1()

    elif choice in answer_B:

        bow1()

    elif choice in answer_C:

        grass1()


def top_floor():

    print(
        "\nEverything is OK - including the bedroom - you wonder why the monster attacked YOUR bedroom?"
    )

    door()


def check_rooms():

    print("\nThe other rooms are fine.")

    door()


#Use sword:


def sword1():

    print("\nIt's too fast! It avoided the attack!")

    bottom_floor()


#Use bow:


def bow1():

    print("\nThe bow landed a hit, and the evil clone of you escaped!")

    print(
        "However, they are not done. They have a castle and are trying to take over the world. If that wasn't enough, the monster that made the hole from earlier is there!"
    )

    print(
        "You entered the castle, as it is nearby, and find the monster that made the hole in your house. It isn't happy, and throws balls made of grass at you. What do you attack them with?"
    )

    print("A. A sword")

    print("B. A bow")

    print("C. A ball made of grass")

    choice = input("Please enter A, B or C: ")

    if choice in answer_A:

        sword2()

    elif choice in answer_B:

        bow2()

    elif choice in answer_C:

        grass2()


#Use grassball:


def grass1():

    print("\nYou don't have any!")

    bottom_floor()

    #Use sword:


def sword2():

    print(
        "\nYou deflected the attack with your sword! You kept deflecting the attacks and defeated it."
    )

    print(
        "You went into a kitchen, and there's clones of you with a chef's hat on. If that wasn't funny enough, there's also a few clones of you with shovels who could just get a sword when fighting but they don't!"
    )

    print(
        "\nWhatever attack you used, you defeated the evil clones and found a king of them. It is way tougher and you need to defeat it. What weapon will you use to defeat it?"
    )

    print("A. A sword")

    print("B. A bow")

    print("C. A ball made of grass")

    choice = input("Please enter A, B or C: ")

    if choice in answer_A:

        sword3()

    elif choice in answer_B:

        bow3()

    elif choice in answer_C:

        grass3()

    #Use bow:


def bow2():

    print(
        "\nThe arrow was too weak. The monster threw a grassball and when the arrow hit it, it got weaker."
    )

    bow1()

    #Use grassball:


def grass2():

    print("\nIt collided with the one the monster thew!")

    bow1()

    #Use sword:


def sword3():

    print(
        "\nAfter a lot of hitting, you defeated the king of all the evil clones of you!"
    )


#Use bow:


def bow3():

    print(
        "\nAfter a lot of shooting, you defeated the king of all the evil clones of you!"
    )

    #Use grassball:


def grass3():

    print(
        "\nThe king of the evil clones is too powerful! It doesn't do anything!"
    )

    sword2()


#This calls the start function, to begin the game:

Start()
