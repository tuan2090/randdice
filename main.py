# Roll the dice simulatorr
from random import randint, seed
from time import time_ns
from os import system

#====== Init dice shape ======#

dices_shape = [
    """
    ==========
    ==========
    ====@@====
    ==========
    ==========
    """,
    """
    ==========
    ==========
    ==@@==@@==
    ==========
    ==========
    """,
    """
    ==========
    ====@@====
    ==========
    ==@@==@@==
    ==========
    """,
    """
    ==========
    ==@@==@@==
    ==========
    ==@@==@@==
    ==========
    """,
    """
    ==========
    ==@@==@@==
    ====@@====
    ==@@==@@==
    ==========
    """,
    """
    ==========
    ==@@==@@==
    ==@@==@@==
    ==@@==@@==
    ==========
    """
]

#====== Function ======#

def do_print_bar():
    print("====================")

def do_clear_screen():
    system("clear")

def do_random_dice(dices):
    do_print_bar()

    random_num = randint(0, 5)
    random_dice = dices[random_num]

    print(random_dice)

    do_print_bar()

def do_more_random_dice(dices, amount):
    do_print_bar()

    for i in range(amount):
        do_print_bar()

        seed(time_ns())
        random_num = randint(0, 5)
        random_dice = dices[random_num]

        print(f"Dice {i+1}:\n{random_dice}")

    do_print_bar()

#====== Program ======#
print("""Roll the dice simulator
Enter 'x' to quit
Enter 'rdice' to roll 1 dice
Enter 'rmdice' to roll more 1 dice
""")

while True:
    cmd = input()

    do_clear_screen()

    if cmd == "x":
        break

    elif cmd == "rdice":
        do_random_dice(dices_shape)
        continue

    else:
        cmd = input("Enter amount of dice: ")
        do_clear_screen()
        do_more_random_dice(dices_shape, int(cmd))
        continue
