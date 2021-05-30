import random as r


class monster:
    def __init__(self, name, hp, attack, attack_cost, heal, heal_cost, type_):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.attack_cost = attack_cost
        self.heal_cost = heal_cost
        self.heal = heal
        self.type = type_

class energy:
    def __init__(self, name, type_, amount):
        self.name = name
        self.type = type_
        self.amount = amount

class special:
    def __init__(self, name, type_, amount):
        self.name = name
        self.type = type_
        self.amount = amount

class unforeseen_event:
    def __init__(self, name, type_, amount):
        self.name = name
        self.type = type_
        self.amount = amount

'''---------------------------------------------------------------------------------------------------------------------
-----------------------------END CARD CLASSES-------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
'''



name_input1 = input('PLAYER 1 Enter the name of your monsters here:')
name_input2 = input('PLAYER 2 Enter the name of your monsters here:')

tko_str_check_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# sets number of knockouts to win--------------------------------------------------------------------------------------

while True:
    tko_amount_str = input("Enter number of knockouts needed to win (1-10) here")
    if tko_amount_str not in tko_str_check_list:
        print('Did not understand, try again.')
        continue
    tko_amount = int(tko_amount_str)
    break

# sets how many cards to fill in each deck-----------------------------------------------------------------------------

print('\nPlease choose how many cards to fill the deck with (10-100).\n')

card_fill_check = [num for num in range(10, 101)]
card_fill_check_str_list = []

for num in card_fill_check:
    card_fill_check_str_list.append(str(num))

card_fill_check_str = ''.join(card_fill_check_str_list)


while True:
    deck_fill_num_str = input('Enter number of cards to fill decks with here:')

    if deck_fill_num_str not in card_fill_check_str:
        print('\nNot a valid entry.\n')
        continue

    deck_fill_num = int(deck_fill_num_str)
    if deck_fill_num not in card_fill_check:
        print('\nNot a valid entry.\n')
        continue

    break

'''
========================================== SETS NUMBER OF CARD TYPES IN EACH DECK ======================================
                                                       PLAYER 1                                                         
'''

print(f'\n======================================= PLAYER 1 ====================================================\n'
      f'\nThere are 3 different types of cards to fill the deck with. Monster cards, Energy cards, and Special cards.\n'
      f'PLAYER 1 please enter the amount of each type of card you would like in your deck (deck = {deck_fill_num}).\n'
      f'=====================================================================================================\n')

player_str = 'PLAYER 1'

# number of monster cards player 1 -------------------------------------------------------------------------------------

while True:
    user_mon_num_str1 = input(f"{player_str}, please enter the number of monsters "
                              f"you want in your deck ({deck_fill_num - 2} maximum):")

    if user_mon_num_str1 not in card_fill_check_str:
        print('\nNot a valid entry\n')
        continue

    user_mon_num1 = int(user_mon_num_str1)
    if user_mon_num1 > deck_fill_num - 2:
        print('Number is too high.')
        continue

    if user_mon_num1 < 1:
        print('Number is too low.')
        continue

    break

# ask number of energy cards ---------------------------------------------------------------------------------------

pot_energy1 = deck_fill_num - user_mon_num1

while True:
    user_energy_num_str1 = input(f"{player_str}, please enter the number of energy "
                             f"you want in your deck ({pot_energy1 - 1} maximum):")

    if user_energy_num_str1 not in card_fill_check_str:
        print('\nNot a valid entry\n')
        continue

    user_energy_num1 = int(user_energy_num_str1)
    if user_energy_num1 > pot_energy1 - 1:
        print('Number is too high.')
        continue

    if user_energy_num1 < 1:
        print('Number is too low.')
        continue

    break

user_special_num1 = pot_energy1 - user_energy_num1

'''
========================================== SETS NUMBER OF CARD TYPES IN EACH DECK ======================================
                                                         PLAYER 2
'''


print(f'\n===================================== PLAYER 2 ======================================================\n'
      f'\nThere are 3 different types of cards to fill the deck with. Monster cards, Energy cards, and Special cards.\n'
      f'PLAYER 1 please enter the amount of each type of card you would like in your deck (deck = {deck_fill_num}).\n'
      f'=====================================================================================================\n')

player_str = 'PLAYER 2'

# number of monster cards player 2 -------------------------------------------------------------------------------------

while True:
    user_mon_num_str2 = input(f"{player_str}, please enter the number of monsters "
                              f"you want in your deck ({deck_fill_num - 2} maximum):")

    if user_mon_num_str2 not in card_fill_check_str:
        print('\nNot a valid entry\n')
        continue

    user_mon_num2 = int(user_mon_num_str2)
    if user_mon_num2 > deck_fill_num - 2:
        print('Number is too high.')
        continue

    if user_mon_num2 < 1:
        print('Number is too low.')
        continue

    break

# ask number of energy cards ---------------------------------------------------------------------------------------

pot_energy2 = deck_fill_num - user_mon_num2

while True:
    user_energy_num_str2 = input(f"{player_str}, please enter the number of energy "
                                 f"you want in your deck ({pot_energy2 - 1} maximum):")

    if user_energy_num_str2 not in card_fill_check_str:
        print('\nNot a valid entry\n')
        continue

    user_energy_num2 = int(user_energy_num_str2)
    if user_energy_num2 > pot_energy2 - 1:
        print('Number is too high.')
        continue

    if user_energy_num2 < 1:
        print('Number is too low.')
        continue

    break

user_special_num2 = pot_energy2 - user_energy_num2


special_list1 = [special('draw 1 card', 'draw', 1),
                special('draw 2 cards', 'draw', 2),
                special('draw 3 cards', 'draw', 3),
                special('draw 1 energy card', 'draw energy', 1),
                special('draw 2 energy cards', 'draw energy', 2),
                special('draw 3 energy card', 'draw energy', 3),
                special(f'draw 1 {name_input1} card', 'draw monster', 1),
                special(f'draw 2 {name_input1} cards', 'draw monster', 2),
                special('draw 1 special card', 'draw special', 1),
                special('draw 2 special cards', 'draw special', 2),
                special('attack +20', 'attack', 20),
                special('attack +50', 'attack', 50),
                special('heal +20', 'heal', 20),
                special('heal +50', 'heal', 50),
                special('pickup 1 from discard pile', 'discard', 1),
                special('pickup 2 from discard pile', 'discard', 2)]

special_list2 = [special('draw 1 card', 'draw', 1),
                special('draw 2 cards', 'draw', 2),
                special('draw 3 cards', 'draw', 3),
                special('draw 1 energy card', 'draw energy', 1),
                special('draw 2 energy cards', 'draw energy', 2),
                special('draw 3 energy card', 'draw energy', 3),
                special(f'draw 1 {name_input2} card', 'draw monster', 1),
                special(f'draw 2 {name_input2} cards', 'draw monster', 2),
                special('draw 1 special card', 'draw special', 1),
                special('draw 2 special cards', 'draw special', 2),
                special('attack +20', 'attack', 20),
                special('attack +50', 'attack', 50),
                special('heal +20', 'heal', 20),
                special('heal +50', 'heal', 50),
                special('pickup 1 from discard pile', 'discard', 1),
                special('pickup 2 from discard pile', 'discard', 2)]

energy_list = [energy('1 water energy', 'water', 1),
               energy('2 water energy', 'water', 2),
               energy('3 water energy', 'water', 3),
               energy('1 earth energy', 'earth', 1),
               energy('2 earth energy', 'earth', 2),
               energy('3 earth energy', 'earth', 3),
               energy('1 fire energy', 'fire', 1),
               energy('2 fire energy', 'fire', 2),
               energy('3 fire energy', 'fire', 3),
               energy('1 any type energy', 'any', 1),
               energy('2 any type energy', 'any', 2),
               energy('3 any type energy', 'any', 3)]

monster_list1 = [monster(f'fluffy WATER {name_input1}',     125, 25,  1, 25, 1, "water"),
                 monster(f'fluffy WATER {name_input1}',     125, 25,  1, 25, 1, "water"),
                 monster(f'fluffy WATER {name_input1}',     125, 25,  1, 25, 1, "water"),
                 monster(f'ferocious WATER {name_input1}',  75,  75,  3, 50, 2, "water"),
                 monster(f'ferocious WATER {name_input1}',  75,  75,  3, 50, 2, "water"),
                 monster(f'ferocious WATER {name_input1}',  75,  75,  3, 50, 2, "water"),
                 monster(f'cute lil WATER {name_input1}',   100, 50,  2, 50, 2, "water"),
                 monster(f'cute lil WATER {name_input1}',   100, 50, 2, 50, 2, "water"),
                 monster(f'cute lil WATER {name_input1}',   100, 50, 2, 50, 2, "water"),
                 monster(f'fluffy EARTH {name_input1}',     125, 25,  1, 25, 1, "earth"),
                 monster(f'fluffy EARTH {name_input1}',     125, 25,  1, 25, 1, "earth"),
                 monster(f'fluffy EARTH {name_input1}',     125, 25,  1, 25, 1, "earth"),
                 monster(f'ferocious EARTH {name_input1}',  75,  75,  3, 50, 2, "earth"),
                 monster(f'ferocious EARTH {name_input1}',  75,  75,  3, 50, 2, "earth"),
                 monster(f'ferocious EARTH {name_input1}',  75,  75,  3, 50, 2, "earth"),
                 monster(f'cute lil EARTH {name_input1}',   100, 50,  2, 50, 2, "earth"),
                 monster(f'cute lil EARTH {name_input1}',   100, 50, 2, 50, 2, "earth"),
                 monster(f'cute lil EARTH {name_input1}',   100, 50, 2, 50, 2, "earth"),
                 monster(f'fluffy FIRE {name_input1}',      125, 25,  1, 25, 1, "fire"),
                 monster(f'fluffy FIRE {name_input1}',      125, 25,  1, 25, 1, "fire"),
                 monster(f'fluffy FIRE {name_input1}',      125, 25,  1, 25, 1, "fire"),
                 monster(f'ferocious FIRE {name_input1}',   75,  75,  3, 50, 2, "fire"),
                 monster(f'ferocious FIRE {name_input1}',   75,  75,  3, 50, 2, "fire"),
                 monster(f'ferocious FIRE {name_input1}',   75,  75,  3, 50, 2, "fire"),
                 monster(f'cute lil FIRE {name_input1}',    100, 50,  2, 50, 2, "fire"),
                 monster(f'cute lil FIRE {name_input1}',    100, 50,  2, 50, 2, "fire"),
                 monster(f'cute lil FIRE {name_input1}',    100, 50,  2, 50, 2, "fire")]

monster_list2 = [monster(f'fluffy WATER {name_input2}',     125, 25,  1, 25, 1, "water"),
                 monster(f'fluffy WATER {name_input2}',     125, 25,  1, 25, 1, "water"),
                 monster(f'fluffy WATER {name_input2}',     125, 25,  1, 25, 1, "water"),
                 monster(f'ferocious WATER {name_input2}',  75,  75,  3, 50, 2, "water"),
                 monster(f'ferocious WATER {name_input2}',  75,  75,  3, 50, 2, "water"),
                 monster(f'ferocious WATER {name_input2}',  75,  75,  3, 50, 2, "water"),
                 monster(f'cute lil WATER {name_input2}',   100, 50,  2, 50, 2, "water"),
                 monster(f'cute lil WATER {name_input2}',   100, 50, 2, 50, 2, "water"),
                 monster(f'cute lil WATER {name_input2}',   100, 50, 2, 50, 2, "water"),
                 monster(f'fluffy EARTH {name_input2}',     125, 25,  1, 25, 1, "earth"),
                 monster(f'fluffy EARTH {name_input2}',     125, 25,  1, 25, 1, "earth"),
                 monster(f'fluffy EARTH {name_input2}',     125, 25,  1, 25, 1, "earth"),
                 monster(f'ferocious EARTH {name_input2}',  75,  75,  3, 50, 2, "earth"),
                 monster(f'ferocious EARTH {name_input2}',  75,  75,  3, 50, 2, "earth"),
                 monster(f'ferocious EARTH {name_input2}',  75,  75,  3, 50, 2, "earth"),
                 monster(f'cute lil EARTH {name_input2}',   100, 50,  2, 50, 2, "earth"),
                 monster(f'cute lil EARTH {name_input2}',   100, 50, 2, 50, 2, "earth"),
                 monster(f'cute lil EARTH {name_input2}',   100, 50, 2, 50, 2, "earth"),
                 monster(f'fluffy FIRE {name_input2}',      125, 25,  1, 25, 1, "fire"),
                 monster(f'fluffy FIRE {name_input2}',      125, 25,  1, 25, 1, "fire"),
                 monster(f'fluffy FIRE {name_input2}',      125, 25,  1, 25, 1, "fire"),
                 monster(f'ferocious FIRE {name_input2}',   75,  75,  3, 50, 2, "fire"),
                 monster(f'ferocious FIRE {name_input2}',   75,  75,  3, 50, 2, "fire"),
                 monster(f'ferocious FIRE {name_input2}',   75,  75,  3, 50, 2, "fire"),
                 monster(f'cute lil FIRE {name_input2}',    100, 50,  2, 50, 2, "fire"),
                 monster(f'cute lil FIRE {name_input2}',    100, 50,  2, 50, 2, "fire"),
                 monster(f'cute lil FIRE {name_input2}',    100, 50,  2, 50, 2, "fire")]

unforeseen_variable_list = [unforeseen_event('flood', 'water', 30),
                            unforeseen_event('storm', 'water', 15),
                            unforeseen_event('firestorm', 'fire', 30),
                            unforeseen_event('fire', 'fire', 15),
                            unforeseen_event('earthquake', 'earth', 30),
                            unforeseen_event('landslide', 'earth', 15)]



# empty list of player decks
deck1 = []
deck2 = []

# empty list of cards in hand
hand1 = []
hand2 = []

# empty list of cards in play
in_play1 = []
in_play2 = []

# empty list of energy in play
energy_in_play1 = {'water' : 0, 'fire' : 0, 'earth' : 0, 'any' : 0}
energy_in_play2 = {'water' : 0, 'fire' : 0, 'earth' : 0, 'any' : 0}

# empty list of discard pile
discard1 = []
discard2 = []

# unforeseen variable list
unforeseen_variable = []

# knockout count
tko1 = 0
tko2 = 0

# numb check
num_check = '012345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455'
'''
==============================FILL DECK FUNCTION========================================================================
fill_deck() function will fill a specified 'list' (or deck) with 3 types of cards.


parameters = 
              monster_num :     an 'int' that defines the number of monster cards to fill the deck with
              energy_num :      an 'int' that defines the number of energy cards to fill the deck with
              special_num :     an 'int' that defines the number of special cards to fill the deck with

              deck :             a 'list' (or deck) that you would like to fill with the above mentioned cards


returns = 'NONE'
'''


def fill_deck(monster_num, monster_deck, energy_num, special_num, special_deck, deck):
    for num in range(monster_num):
        random_ind = r.randint(0, len(monster_deck) - 1)
        deck.append(monster_deck.pop(random_ind))

    for num in range(energy_num):
        random_energy = r.choice(energy_list)
        deck.append(random_energy)

    for num in range(special_num):
        random_special = r.choice(special_deck)
        deck.append(random_special)


'''
========================================= END FUNCTION =================================================================
'''
'''
===================================== DRAW_CARD_TYPE FUNCTION ==========================================================
draw_card_type(): function will pop and remove a given number of cards of a specified type from a given list and 
                   append them to another given list.


parameters = 
             num :              an 'int' that specifies the amount of cards to pop from the given list

             from_card_list :    a 'list' that you want to pop these cards from
             to_card_list :      a 'list' that you want the popped cards to append too

             type_ :             a 'class type' that you want the function to search for from the given list 


returns = 'NONE'
'''


def draw_card_type(num, from_card_list, to_card_list, type_):
    card_counter = 0
    card_index_list = []

    for i, card in enumerate(from_card_list):
        if type(card) == type_:
            card_counter += 1
            card_index_list.append(i)

    if card_counter < num:
        num = card_counter

    if len(card_index_list) > 0:
        for number in range(num):
            random_index_choice = r.choice(card_index_list)
            card_index_list.remove(random_index_choice)
            to_card_list.append(from_card_list.pop(random_index_choice))


'''
========================================== END FUNCTION ================================================================
'''
'''
======================================== DRAW_CARDS FUNCTION ===========================================================
draw_cards(): function draws a specified number of random cards from a given list into a specified list


parameters =
            num :               an "int' defining the number of cards to draw
            from_card_list :    a 'list' you want the cards popped out of
            to_card_list :      a 'list' you want the popped cards appended too

returns = 'NONE'
'''


def draw_cards(num, from_card_list, to_card_list):
    for number in range(num):
        random_num = r.randint(0, len(from_card_list) - 1)
        to_card_list.append(from_card_list.pop(random_num))


'''
====================================== END FUNCTION ====================================================================
'''
'''
============================= PRINT_MONSTER_CARDS FUNCTION =============================================================
def print_monster_cards():  Prints only monster cards from a list with all the monster card attributes. Stores the 
                            indices of monster cards in a monster_card_check 'list' within function.


parameters =        
                     monster_ind_check_list :    a list to store indices of monster cards in order to check

                     card_list :        a 'list' to search for 'monster' class.

returns =            'None'
'''


def print_monster_cards_and_check(monster_ind_check_list, card_list):
    for i, monster_ in enumerate(card_list):
        if type(monster_) == monster:
            monster_ind_check_list.append(i)
            print(f'card number = {i} \n'
                  f'name =        {monster_.name} \n'
                  f'HP =          {monster_.hp} \n'
                  f'ATTACK =      {monster_.attack} \n'
                  f'attack cost = {monster_.attack_cost} energy \n'
                  f'HEAL =        {monster_.heal} \n'
                  f'heal cost =   {monster_.heal_cost} energy \n'
                  f'type =        {monster_.type} \n\n')


'''
====================================== END FUNCTION ====================================================================
'''
'''
============================CREATE_UNFORESEEN_VARIABLE==================================================================
create_unforeseen_variable(): function generates a random number between 1 and 10. If the number is greater than 7 the 
                              function appends an unforeseen event class card into the unforeseen variable "list".

parameters   =     'NONE'

returns      =     'NONE'

'''


def create_unforeseen_variable():
    random_number10 = r.randint(1, 10)
    if random_number10 > 7:
        unforeseen_variable.append(r.choice(unforeseen_variable_list))


'''
=================================== END OF FUNCTION =====================================================================
'''
'''
===================================== PRINT SPECIAL CARD FUNCTION ======================================================
print_special_cards(): function prints out all special cards from a specified list. Also adds the index number of all 
                    special cards to "special_card_check" list. Takes special_check argument and returns True or False 
                    depending on if the card is in the check list or not.

parameters = 
                 special_ind_check :    a list that special card indices are appended too

                 card_list :            a 'list' to search within for 'special' card class.

returns =        'None'
'''


def print_special_cards(special_ind_check, card_list):
    for i, special_ in enumerate(card_list):
        if type(special_) == special:
            special_ind_check.append(i)
            print(f'card number = {i} \n'
                  f'{special_.name} \n')



'''
========================================= END FUNCTION =================================================================
'''
'''
====================================== Print energy card type function =================================================
def print_energy_card_type(): prints energy cards of a given type from a given list and adds indices to given check list

parameters:   
            card_list:               list to iterate through and search for energy cards
            energy_card_check:       list to add indices of energy cards
            type_:                   string to check type of energy to search for
            
returns: 
            'None'

'''


# prints specific type energy cards out of given list
def print_energy_cards_type(card_list, energy_card_check, type_):
    for i, energy_ in enumerate(card_list):
        if type(energy_) == energy and energy_.type == type_:
            energy_card_check.append(i)
            print(f'card number = {i} \n'
                  f'{energy_.name} \n')

'''
======================== END OF FUNCTION ===============================================================================
'''
'''
====================================== Print energy function =================================================
def print_energy(): prints energy cards from a given list and adds indices to given check list

parameters:   
            card_list:               list to iterate through and search for energy cards
            energy_card_check:       list to add indices of energy cards

returns: 
            'None'

'''


# prints specific type energy cards out of given list
def print_energy(card_list, energy_card_check2):
    for i, energy_ in enumerate(card_list):
        if type(energy_) == energy:
            energy_card_check2.append(i)
            print(f'card number = {i} \n'
                  f'{energy_.name} \n')


'''
======================== END OF FUNCTION ===============================================================================
'''
# GAME________________________________________ Player One fill decks and hand___________________________________________

# Fills deck1 with cards
fill_deck(user_mon_num1, monster_list1, user_energy_num1, user_special_num1, special_list1, deck1)

# pops 1 monster card from deck into hand
draw_card_type(1, deck1, hand1, monster)

# draws 6 cards into player 1 hand
draw_cards(6, deck1, hand1)

# print out cards in player hand
print(f'\n========== Player 1 hand ================\n')
for card_ in hand1:
    print(card_.name)
print('\n========== End PLayer hand ================')

# Asks player to choose a monster card
print(f'\nPLAYER 1 CHOOSE {name_input1} CARD TO PUT INTO PLAY. \n')


monster_ind_check = []
print_monster_cards_and_check(monster_ind_check, hand1)

while True:

    user_input = input(f"Enter card number here Player 1:")
    if user_input not in num_check:
        continue

    user_input_int = int(user_input)
    if user_input_int not in monster_ind_check:
        continue

    # appends chosen card to player hand
    in_play1.append(hand1.pop(user_input_int))

    print(f'\nPLAYER 1 PUTS {in_play1[0].name} INTO PLAY!\n')
    break

# GAME________________________________________ Player Two fill decks and hand __________________________________________

# Fills deck2 with cards
fill_deck(user_mon_num2, monster_list2, user_energy_num2, user_special_num2, special_list2, deck2)

# pops 1 monster card from deck into hand
draw_card_type(1, deck2, hand2, monster)

# draws 6 cards into player 2 hand
draw_cards(6, deck2, hand2)

# print out cards in player hand
print(f'\n========== Player 2 hand ================\n')
for card_ in hand2:
    print(card_.name)
print('\n========== End Player hand ================')

# Asks player to choose a monster card
print(f'\nPLAYER 2 CHOOSE {name_input2} CARD TO PUT INTO PLAY. \n')

# while loop to ensure user_input is usable as well as prints out cards to choose from and stores user input
monster_ind_check = []
print_monster_cards_and_check(monster_ind_check, hand2)

while True:

    user_input = input(f"Enter card number here Player 2:")
    if user_input not in num_check:
        continue

    user_input_int = int(user_input)
    if user_input_int not in monster_ind_check:
        continue

    # appends chosen card to player hand
    in_play2.append(hand2.pop(user_input_int))

    print(f'\nPLAYER 2 PUTS {in_play2[0].name} INTO PLAY!\n')
    break

# END ------------------------------------------------------------------------------------------------------------------


'''
============================================== GAME LOOP START =========================================================
------------------------------------------------------------------------------------------------------------------------'''

# game counter, boolean, and check
game_check = False
game = True
game_counter = 0

# ----------------------------------------------------------------------------------------------------------------------

while game:

    # Clears previous unforeseen event
    unforeseen_variable.clear()

    # creates an unforeseeable event at random before player turns
    create_unforeseen_variable()

# -----------------------------------------PRE PLAYER 1 LOOP TURN ------------------------------------------------------

    # sets counts, counters for player 1
    special_card_count1 = 0
    retreat_count1 = 0
    heal_counter1 = 0
    energy_counter1 = 0

    # sets counts, counters for player 2
    special_card_count2 = 0
    retreat_count2 = 0
    heal_counter2 = 0
    energy_counter2 = 0


    # sets card check variables
    energy_card_check = []

    # switches back and forth between player 1 and 2 -------------------------------------------------------------------
    if game_counter % 2 == 0:

        # sets up deck, card lists, and string variables player 1
        player_deck = deck1
        player_hand = hand1
        player_in_play = in_play1
        player_discard = discard1
        player_string = "PLAYER 1"
        opp_hand = hand2
        opp_in_play = in_play2
        opp_discard = discard2
        opp_string = "PLAYER 2"
        energy_in_play = energy_in_play1
        opp_energy_in_play = energy_in_play2
        special_card_count= special_card_count1
        retreat_count = retreat_count1
        heal_counter = heal_counter1
        energy_counter = energy_counter1
        tko = tko1
        opp_tko = tko2
        name_input = name_input1
        opp_name_input = name_input2

    if game_counter % 2 != 0:
        # sets up deck, card lists, and string variables2
        player_deck = deck2
        player_hand = hand2
        player_in_play = in_play2
        player_discard = discard2
        player_string = "PLAYER 2"
        opp_hand = hand1
        opp_in_play = in_play1
        opp_discard = discard1
        opp_string = "PLAYER 1"
        energy_in_play = energy_in_play2
        opp_energy_in_play = energy_in_play1
        special_card_count = special_card_count2
        retreat_count = retreat_count2
        heal_counter = heal_counter2
        energy_counter = energy_counter2
        tko = tko2
        opp_tko = tko1
        name_input = name_input2
        opp_name_input = name_input1

    print('---------------------------'
          '----------------------------'
          '----------------------------'
          '-------------------------')

    # check to see if deck is empty ------------------------------------------------------------------------------------
    if len(player_deck) < 1:
        print(f'\n{player_string} is out of cards!!!!\n\n'
              f'{opp_string} wins!!!\n'
              f'{opp_string} wins!!!\n'
              f'{opp_string} wins!!!\n')
        break



    # draw cards from deck----------------------------------------------------------------------------------------------

    draw_cards(1, player_deck, player_hand)
    print(f'\n{player_string} draws \'{player_hand[-1].name}\' card!\n')

    # ------------------------------------------------------------------------------------------------------------------

    # checks for player monster in play if none and no monsters in hand opponent wins. If monster in hand, chooses
    if len(player_in_play) == 0:

        hand_check = 0
        for monster_ in player_hand:
            if type(monster_) == monster:
                hand_check += 1

        if hand_check < 1:
            print(f'\n{player_string} is out of {name_input}!!!!\n\n'
                  f'{opp_string} wins!!!\n'
                  f'{opp_string} wins!!!\n'
                  f'{opp_string} wins!!!\n')
            break

        # print out cards in player hand
        print(f'\n{player_string} hand =\n')
        for card_ in player_hand:
            print(card_.name)

        # Asks player to choose a monster card
        print(f'\n{player_string} choose {name_input} card to put into play \n')

        # while loop to ensure user_input is usable as well as prints out cards to choose from and stores user input
        monster_ind_check = []
        print_monster_cards_and_check(monster_ind_check, player_hand)

        # choose monster loop ------------------------------------------------------------------------------------------

        while True:

            user_input = input(f"Enter card number here {player_string}:")
            if user_input not in num_check:
                continue

            user_input_int = int(user_input)
            if user_input_int not in monster_ind_check:
                continue


            # appends chosen card to player hand
            player_in_play.append(player_hand.pop(user_input_int))

            print(f'{player_string} puts {player_in_play[0].name} into play!\n\n')
            break

# ---------------------------------------- Player loop turn start ------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    while True:

        turn_check = False

        event = ''
        type_event = ''
        amount_event = ''

        if len(unforeseen_variable) > 0:
            event = {unforeseen_variable[0].name}
            type_event = {unforeseen_variable[0].type}
            amount_event = {unforeseen_variable[0].amount}


        # print out cards in player hand
        print(f'\n========== {player_string} hand =================\n')
        for card_ in player_hand:
            print(card_.name)
        print('\n========== End hand =========================')

        print(f'\nPLAYER 1 ENERGY = {energy_in_play1}')
        print(f'PLAYER 2 ENERGY = {energy_in_play2}')

        # Prints both players in play cards and takes user input on what move to make-------------------------------
        print(f'\n {player_string} IT IS YOUR TURN TO PLAY ----------------------------------------------- \n\n'
        f'                PLAYER 1 ({len(deck1)})               PLAYER 2 ({len(deck2)})                        EVENT\n'
        f'         {in_play1[0].name}          {in_play2[0].name}             {event} \n'
        f'HP              = {in_play1[0].hp}                    {in_play2[0].hp}                              {type_event}  \n'
        f'ATTACK          = {in_play1[0].attack}                     {in_play2[0].attack}                               {amount_event} \n'
        f'Attack Cost     = {in_play1[0].attack_cost}                      {in_play2[0].attack_cost}\n'
        f'HEAL            = {in_play1[0].heal}                     {in_play2[0].heal} \n'
        f'Heal Cost       = {in_play1[0].heal_cost}                      {in_play2[0].heal_cost}  \n\n'


                  f'Type \'R\' to retreat, \'A\' to attack, \'H\' to heal,\n'
                  f' \'S\' to play a special card, \'E\' to put energy in play, or \'N\' to end your turn.\n'
                  f'---------------------------------------------------------------------------------')

        while True:
            user_input1 = input("Enter move here:")

            if user_input1 not in 'rRhHsSnNaAeE':
                print(f'\n{player_string} you must be speaking in russian, I can\'t understand your move!\n'
                      f'Please try again!\n')
                continue

            if user_input1 == 'n' or user_input1 == 'N':
                print(f' \n {player_string} your turn is over.\n')
                turn_check = True
                break
            break

        if turn_check:
            break
        # -----------------------------------------Put Energy In Play---------------------------------------------------

        if user_input1 == 'e' or user_input1 == 'E':
            if energy_counter > 0:
                print(f'\n{player_string} you have already put energy into play this turn. Be patient!!!!\n')
                continue

            energy_index_check = []
            print_energy(player_hand, energy_index_check)

            if len(energy_index_check) < 1:
                print('\nYou have no energy!\n')
                continue

            while True:

                user_energy_input = input(f'{player_string} enter card number to put into play here or \'N\' to skip:')
                if user_energy_input in 'nN':
                    turn_check = False
                    break

                if user_energy_input not in num_check:
                    print(f'Invalid card number, please try again.')
                    continue

                user_energy_int = int(user_energy_input)
                if user_energy_int not in energy_index_check:
                    print(f'Invalid card number, please try again.')
                    continue

                energy_card = player_hand[user_energy_int]
                energy_type = energy_card.type
                energy_amount = energy_card.amount

                energy_in_play[energy_type] += energy_amount
                player_discard.append(player_hand.pop(user_energy_int))
                print(f'\n{player_string} ENERGY = \n'
                      f'{energy_in_play}\n')
                energy_counter += 1
                turn_check = True
                break

        if turn_check:
            continue

        # ------------------------------------------------ Retreat -----------------------------------------------------

        if user_input1 == 'r' or user_input1 == 'R':
            if retreat_count > 0:
                print(f'\n{player_string} you are a coward! you can only retreat once per turn!\n')
                continue

            print(f'\n{player_string} retreats {player_in_play[0].name}!\n')
            player_hand.append(player_in_play.pop())
            retreat_count += 1

            monster_ind_check.clear()
            while True:
                print_monster_cards_and_check(monster_ind_check, player_hand)
                if len(monster_ind_check) == 0:
                    print(f'\nOh no!!! you are out of {name_input}!!!!\n')
                    break

                user_input3 = input(f"Enter card number here {player_string} to place new {name_input} in play:")
                if user_input3 not in num_check:
                    monster_ind_check.clear()
                    continue

                user_input3_int = int(user_input3)
                if user_input3_int not in monster_ind_check:
                    monster_ind_check.clear()
                    continue

                else:
                    # appends chosen card to player hand
                    player_in_play.append(player_hand.pop(user_input3_int))

                    print(f'\n{player_string} puts {player_in_play[0].name} into play!\n')
                    break

            continue

        # ------------------------------------- Heal -------------------------------------------------------------------

        if user_input1 == 'h' or user_input1 == 'H':
            if heal_counter > 0:
                print(f'\n{player_string} your {player_in_play[0].name} has already healed this turn!\n')
                continue

            monster_name = player_in_play[0].name
            monster_type = player_in_play[0].type
            heal_cost = player_in_play[0].heal_cost
            heal = player_in_play[0].heal
            any_energy_amount = energy_in_play['any']
            type_energy_amount = energy_in_play[monster_type]
            energy_total_amount = any_energy_amount + type_energy_amount

            if energy_total_amount < heal_cost:
                print(f'\n{player_string} you do not have enough {monster_type} energy!\n')
                continue

            subtract_any_energy = 0
            if type_energy_amount < heal_cost:
                subtract_any_energy = heal_cost - type_energy_amount
                heal_cost = type_energy_amount

            # if there is an unforeseen variable
            if len(unforeseen_variable) > 0:
                event_type = unforeseen_variable[0].type
                event_amount = unforeseen_variable[0].amount

                # adds unforeseen variable amount to attack if player 1 type  and unforeseen variable type is the same
                if event_type == 'water' and monster_type == 'water':
                    heal += event_amount

                if event_type == 'fire' and monster_type == 'fire':
                    heal += event_amount

                if event_type == 'earth' and monster_type == 'earth':
                    heal += event_amount

            energy_in_play[monster_type] -= heal_cost
            energy_in_play['any'] -= subtract_any_energy
            player_in_play[0].hp += heal
            heal_counter += 1
            print(f'\n{monster_name} was healed for {heal}!\n')
            continue

        # ------------------------------------ Play special Card--------------------------------------------------------

        if user_input1 == 's' or user_input1 == 'S':

            if special_card_count1 > 1:
                print("\nYou can only use 2 special cards! Stop thinking only about yourself!\n")
                continue

            special_check = []
            print_special_cards(special_check, player_hand)

            if len(special_check) < 1 :
                print('\n You have no special cards to play!!!!\n')
                continue

            while True:
                special_input = input(f'\n Enter card # to play or \'N\' to skip:')

                if special_input in 'nN':
                    turn_check = True
                    break

                elif special_input in num_check:
                    # change string to 'int' type
                    special_input = int(special_input)

                    if special_input not in special_check:
                        print('\nWrong card number, please try again.\n')
                        continue

                    card_type = type(player_hand[special_input])
                    special_type = player_hand[special_input].type

                    if card_type == special and special_type == 'draw':
                        amount = player_hand[special_input].amount
                        print(f'\n {player_string} draws {amount} cards! \n')
                        player_discard.append(player_hand.pop(special_input))
                        special_card_count1 += 1
                        draw_cards(amount, player_deck, player_hand)
                        turn_check = True
                        break

                    # draws (user_input) energy cards into player hand
                    if card_type == special and special_type == 'draw energy':
                        amount = player_hand[special_input].amount
                        print(f'\n {player_string} draws {amount} energy cards! \n')
                        player_discard.append(player_hand.pop(special_input))
                        special_card_count1 += 1
                        draw_card_type(amount, player_deck, player_hand, energy)
                        turn_check = True
                        break

                    # draws (user_input) monster cards into player hand
                    if card_type == special and special_type == f'draw monster':
                        amount = player_hand[special_input].amount
                        print(f'\n {player_string} draws {amount} {name_input} cards! \n')
                        player_discard.append(player_hand.pop(special_input))
                        special_card_count1 += 1
                        draw_card_type(amount, player_deck, player_hand, monster)
                        turn_check = True
                        break

                    # draws (user_input) special cards into player hand
                    if card_type == special and special_type == 'draw special':
                        amount = player_hand[special_input].amount
                        print(f'\n {player_string} draws {amount} special cards! \n')
                        player_discard.append(player_hand.pop(special_input))
                        special_card_count1 += 1
                        draw_card_type(amount, player_deck, player_hand, special)
                        turn_check = True
                        break

                    # draws (user_input) special cards into player hand
                    if card_type == special and special_type == 'discard':
                        amount = player_hand[special_input].amount
                        if len(player_discard) == 0:
                            print(f'{player_string} discard pile is empty!')
                            break
                        if len(player_discard) < amount:
                            amount = len(player_discard)
                        print(f'\n {player_string} draws {amount} from discard pile! \n')
                        draw_cards(amount, player_discard, player_hand)
                        for num in range(1, amount + 1):
                            monst = player_hand[-num]
                            if type(monst) == monster:
                                if monst.name[0:4] == 'cute':
                                    monst.hp = 115
                                if monst.name[0:4] == 'fluf':
                                    monst.hp = 140
                                if monst.name[0:4] == 'fero':
                                    monst.hp = 90

                        player_discard.append(player_hand.pop(special_input))
                        special_card_count1 += 1
                        turn_check = True
                        break

                    # attacks player in_play for card amount
                    if card_type == special and special_type == 'attack':
                        amount = player_hand[special_input].amount
                        opp_in_play[0].hp -= amount
                        player_discard.append(player_hand.pop(special_input))
                        print(f' \n {opp_in_play[0].name} was attacked for {amount}! \n')
                        special_card_count1 += 1
                        turn_check = True
                        if opp_in_play[0].hp <= 0:
                            discard2.append(opp_in_play.pop())
                            print(f'\nOH NO!!!! {player_string} knocked out {opp_string}\'s {opp_name_input}!!!!')
                            tko += 1
                            if tko == tko_amount:
                                print(f'{player_string} WINS!!!!!!!')
                                print(f'{player_string} WINS!!!!!!!')
                                print(f'{player_string} WINS!!!!!!!')
                                game_check = True
                                break

                            # Asks player to choose a monster card
                            print(f'\n{opp_string} CHOOSE {opp_name_input} CARD TO PUT INTO PLAY. \n')

                            # while loop to ensure user_input is usable as well as prints out cards to choose from and stores user input
                            monster_ind_check = []
                            print_monster_cards_and_check(monster_ind_check, opp_hand)

                            if len(monster_ind_check) < 1:
                                print(f'{player_string} WINS!!!!!!!')
                                print(f'{player_string} WINS!!!!!!!')
                                print(f'{player_string} WINS!!!!!!!')
                                game_check = True
                                break


                            while True:

                                user_input = input(f"Enter card number here {opp_string}:")
                                if user_input not in num_check:
                                    continue

                                user_input_int = int(user_input)
                                if user_input_int not in monster_ind_check:
                                    continue

                                # appends chosen card to player hand
                                opp_in_play.append(opp_hand.pop(user_input_int))

                                print(f'{opp_string}  PUTS {opp_in_play[0].name} INTO PLAY!\n\n')
                                break

                        break

                    # heals player in_play for special card amount
                    if card_type == special and special_type == 'heal':
                        amount = player_hand[special_input].amount
                        player_in_play[0].hp += amount
                        player_discard.append(player_hand.pop(special_input))
                        print(f' \n {player_in_play[0].name} was healed for {amount}! \n')
                        special_card_count1 += 1
                        turn_check = True
                        break

                else:
                    print('\nDid not understand your entry, please try again.\n')
                    continue

            if game_check:
                break

        if turn_check:
            continue

        if game_check:
            break

        #------------------------- Attack! -----------------------------------------------------------------------------

        if user_input1 == 'a' or user_input1 == 'A':

            attack_cost = player_in_play[0].attack_cost
            attack = player_in_play[0].attack
            type_attack = player_in_play[0].type
            type_defend = opp_in_play[0].type

            any_energy_amount = energy_in_play['any']
            type_energy_amount = energy_in_play[type_attack]
            energy_total_amount = any_energy_amount + type_energy_amount

            if energy_total_amount < attack_cost:
                print(f'\n{player_string} you do not have enough {type_attack} energy to attack!\n')
                continue

            subtract_any_energy2 = 0
            if type_energy_amount < attack_cost:
                subtract_any_energy2 = attack_cost - type_energy_amount
                attack_cost = type_energy_amount

            if type_attack == 'water' and type_defend == 'fire':
                attack += 15

            if type_attack == 'fire' and type_defend == 'earth':
                attack += 15

            if type_attack == 'earth' and type_defend == 'water':
                attack += 15

            # if there is an unforeseen variable
            if len(unforeseen_variable) > 0:
                event_type = unforeseen_variable[0].type
                event_amount = unforeseen_variable[0].amount

                # adds unforeseen variable amount to attack if player 1 type  and unforeseen variable type is the same
                if event_type == 'water' and type_attack == 'water':
                    attack += event_amount

                if event_type == 'fire' and type_attack == 'fire':
                    attack += event_amount

                if event_type == 'earth' and type_attack == 'earth':
                    attack += event_amount

                # subtracts unforeseen variable amount from attack if player 2 type is the same as unforeseen variable type
                if event_type == 'water' and type_defend == 'water':
                    attack -= event_amount

                if event_type == 'fire' and type_defend == 'fire':
                    attack -= event_amount

                if event_type == 'earth' and type_defend == 'earth':
                    attack -= event_amount

            opp_in_play[0].hp -= attack
            energy_in_play[type_attack] -= attack_cost
            energy_in_play['any'] -= subtract_any_energy2
            print(f'{player_string}\'s {player_in_play[0].name} attacked {opp_in_play[0].name} for {attack}!!\n')

            if opp_in_play[0].hp <= 0:
                discard2.append(opp_in_play.pop())
                print(f'\nOH NO!!!! {player_string} knocked out {opp_string}\'s {opp_name_input}!!!!')
                tko += 1

                if tko == tko_amount:
                    print(f'{player_string} WINS!!!!!!!')
                    print(f'{player_string} WINS!!!!!!!')
                    print(f'{player_string} WINS!!!!!!!')
                    game_check = True
                    break

                # Asks player to choose a monster card
                print(f'\n{opp_string} CHOOSE {opp_name_input} CARD TO PUT INTO PLAY. \n')

                # while loop to ensure user_input is usable as well as prints out cards to choose from and stores user input
                monster_ind_check = []
                print_monster_cards_and_check(monster_ind_check, opp_hand)

                if len(monster_ind_check) < 1:
                    print(f'{player_string} WINS!!!!!!!')
                    print(f'{player_string} WINS!!!!!!!')
                    print(f'{player_string} WINS!!!!!!!')
                    game_check = True
                    break

                while True:

                    user_input = input(f"Enter card number here {opp_string}:")
                    if user_input not in num_check:
                        continue

                    user_input_int = int(user_input)
                    if user_input_int not in monster_ind_check:
                        continue

                    # appends chosen card to player hand
                    opp_in_play.append(opp_hand.pop(user_input_int))

                    print(f'{opp_string}  PUTS {opp_in_play[0].name} INTO PLAY!\n\n')
                    break

            break
        if game_check:
            break
        #---------------------END OF ATTACK-----------------------------------------------------------------------------
        else:
            print(f'\n{player_string} please try again.')
            continue
    if game_check:
        break
#-------------------------- End of Player 1 Turn -----------------------------------------------------------------------
    print(f'\n{player_string} turn is over!\n')
    game_counter += 1




#-----------------------------------END OF GAME-------------------------------------------------------------------------

print('GAME OVER!!!!')
print('GAME OVER!!!!')
print('GAME OVER!!!!')
print('GAME OVER!!!!')
print('GAME OVER!!!!')
print('GAME OVER!!!!')
print('GAME OVER!!!!')
print('GAME OVER!!!!')
print('GAME OVER!!!!')