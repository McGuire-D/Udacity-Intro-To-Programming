import time
import random
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    items.clear()
    print_pause('\nYou arrive in a forest.\n')
    print_pause('You here a cry asking for help.\n')
    finding_forest()


def finding_forest():
    print_pause('Will you go to their aid?\n')
    decision = input('\n press 1 for yes \n press 2 for no\n')
    if decision == '1':
        print_pause("""
        You run towards the crys of help to
        find a little old lady trying to unload groceries.\n
        """)
        helping_hand()

    elif decision == '2':
        print_pause("""
        You run in the opposite direction
        of the cries of help screaming.\n
        """)
        print_pause("""
        You trip over a tree root that was exposed
        sticking out of the ground and fall.\n
        """)
        print_pause('You fall towards a cliff and cant stop.\n')
        print_pause('you have died.\n')
        print_pause('\nGAME OVER\n')
        start_over()

    else:
        print_pause('I dont understand')
        finding_forest()


def helping_hand():
    print_pause('Do you help the little old lady with her groceries?\n')
    help = input('\n 1 for yes \n 2 for no\n')
    if help == '1':
        print_pause('You help the old lady carry in her groceries.\n')
        print_pause("""
        After you are done she gives you a glowing
        bottle of milk as a way of saying thanks.\n
        """)
        print_pause("""
        You thank the old women for the gift and
        continue through the forest.\n
        """)
        items.append('glowing bottle of milk')
        forest_romp()
    elif help == '2':
        print_pause("""
        You walk away from the poor old women and hear her sob.\n
        """)
        print_pause("""
        You feel terrible, and you should as you
        walk on through the forest.\n
         """)
        forest_romp()
    else:
        print_pause('I dont understand that response.')
        helping_hand()


def forest_romp():
    animal_list = ['chicken', 'Grizzly bear', 'Giant Turkey', 'Squirrel']
    animal = random.choice(animal_list)
    print_pause("""
    As you make your way though the woods you here a roar.\n
    """)
    print_pause(f'You look towards the noise and its a {animal}.\n')
    print_pause(f"""
    The {animal} is in a tree just in front of you
    and starts making its way down.\n
     """)
    if 'glowing bottle of milk' in items:
        print_pause(f"""
        As you see the {animal} make it to the ground
         it starts heading your way.\n
         """)
        print_pause(f"""
        Out of fear and desperation you open the
         glowing bottle of milk, and at the same time you and the
         {animal} come to the same realization.\n
         """)
        print_pause("""
        You dont know whats in the glowing bottle
         of milk but it is rancid.\n
         """)
        print_pause(f"""
        You pass out from the smell and the {animal}
         high tails it away as fast as possible.\n
         """)
        dream_ending()
    else:
        print_pause(f"""
        As you see the {animal} make it to the
         ground it starts heading your way.\n
         """)
        print_pause("""
        It seems karma wants revenge for not
        helping the old lady as you try to turn and run.\n
        """)
        print_pause(f"""
        In your haste to flee from the {animal}
         you run smack into a branch at forehead level knocking
          you to the ground.\n
          """)
        print_pause(f"""
        The {animal} is upon you in seconds,
         there is nothing you can do.\n
         """)
        print_pause('\nGame Over\n')
        start_over()


def dream_ending():
    print_pause("""
    You start to wake up from being knocked out from the smell.
    \n""")
    print_pause('Do you want to wake up?')
    wake_me_up = input(' 1 for yes\n 2 for no\n')
    if wake_me_up == '1':
        print_pause("""
        As you start to wake up you look around and
        are no longer in a forest but your own bed.\n
        """)
        print_pause("""
        You realize the reason the forest was so
        strange was because it was a dream all along.\n
        """)
        print_pause('\nFIN\n')
        start_over()
    elif wake_me_up == '2':
        print_pause("""
        You decide now is not the time to wake up and roll
        over to go back to sleep.\n
        """)
        print_pause("""
        As you rollover to go back to sleep you fall out of
        a bed and are forced to wake up by the fall.\n
        """)
        print_pause("""
        As you start to wake up you look around and
        are no longer in a forest but your own bedroom.\n
        """)
        print_pause("""
        You realize the reason the forest was so
        strange was because it was a dream all along.\n
        """)
        print_pause('\nFIN\n')
        start_over()


def start_over():
    print('Would you like to play again?')
    answer = input(' 1 for yes\n 2 for no\n')
    if answer == '1':
        intro()
    elif answer == '2':
        print_pause('Thanks for playing!')
    else:
        print_pause('I do not understand.')
        start_over()


intro()
