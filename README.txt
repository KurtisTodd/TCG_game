# TCG_game
A python 2-player TCG game just for experimentation, learning, and fun.

***CARD TYPES***----------------------------------------------------------------------------------------------------------------------------

- ENERGY cards 
               * class object    ('class'   = 'energy')
               - name            (.name     = 'str' expressing name of card)
               - type            (.type     = 'str' expressing type of energy = 'water', 'fire', 'earth', 'any')
               - amount          (.amount   = 'int' expressing the amount of units of energy this card contains 1-3)

- MONSTER cards 
               * class object    ('class'      = 'monster')
               - name            (.name        = 'str' expressing name of monster)
               - HP              (.hp          = 'int' expressing the life count of each monster)
               - attack          (.attack      = 'int' expressing amount this monster can attack opponents HP with)
               - attack cost     (.attack_cost = 'int' expressing amount of units of energy each attack requires)
               - heal            (.heal        = 'int' expressing the amount of healing that will be applied to monsters HP)
               - heal cost       (.heal_cost   = 'int' expressing the amount of units of energy each healing requires)
               - type            (.type        = 'str' expressing this monsters elemental type ( 'water', 'fire', 'earth' )

- SPECIAL cards 
               * class object    ('class' = 'special')
               - name            (.name = 'str' expressing name of card)
               - amount          (.amount = 'int' expressing amount of units to perform action with)
               - type            (.type  = 'str' expressing what actions to take  *ex. 'draw'   *ex. 'draw energy' etc)


***STARTUP OF GAME***-------------------------------------------------------------------------------------------------------------------------

-Upon startup, each player must name his/her monsters.
-Both players must decide how many 'knockouts' they are playing to win (up to 10)
-Both players must decide how many cards to fill into their decks (up to 100). 
                      - if either player runs out of cards to to draw, that player will automatically lose! so choose these numbers wisely!!!!

-Each player then decides how many of each card type to fill in to their respective decks independently.
                      - for example, if both players decided on a 60 card deck, PLAYER 1 can choose 20 monsters and 20 energy cards, which will 
                        then fill the remaining 20 with special cards
                      - PLAYER 2 can now choose his number of monsters, energy cards, and special cards independently to fill his /her deck.
                      
- Both decks will be filled with predefined ratios but with random cards within those 3 card classes.
- 6 random cards and one monster card will then be drawn from each deck into each players hand.
- After getting a chance to see the hand, each player will then put a monster card into play.

***TURN START***--------------------------------------------------------------------------------------------------------------------------------

ELEMENTAL LOOP =    fire < water < earth < fire < water < earth < fire < water < earth < fire < water < earth (etc etc)

             or    fire > earth > water > fire > earth > water > fire > earth > water > fire > earth > water (etc etc)
             
             or    Fire has advantage over Earth.      or         Earth has advantage over Water.
                   Earth has advantage over Water.                Water has advantage over Fire.
                   Water has advantage over Fire.                 Fire has advantage over  Earth.
                   

- At the beggining of each turn, there is a 40% chance of an unforeseen event occuring.
                            - Each event has a Type and Amount
                            - Each event can only last one turn
                            - If an event is occuring and your monster and the event share the same type, add the 'event amount' to your monsters 
                               attack for that given turn.
                            - If an event is occuring and your monster and the event share the same type, minus the 'event amount' from opponents
                              attacks.
                              
- During each turn, player can choose to -   
                                           Retreat                x1
                                           Heal                   x1
                                           Play a Special Card    x2
                                           Play an Energy Card    x1
                                           skip turn
                                     or    Attack                 x1        

- You may choose these options in any order you wish with but one stipulation. When and if you attack, (not including playing a 'special' attack card)
  you are forfeiting the rest of your turn.
  
    
    
***RETREAT***
- You may retreat once per turn and choose another monster to out into play.

***PLAY AN ENERGY CARD***
- Once per turn, you may play an energy card. EAch player has an energy "bank" or "reserve". When you play an energy card, the amount of energy
  shown on the card will be added to the corresponding energy type in your bank.
                                            - For example = If you play a "2 fire energy" card, 2 units of fire energy will be added to your 'fire'
                                               energy "bank" or "reserve." You can keep an infinite number of energy in your bank. Each time you
                                               attack or heal, it will require energy from your bank to perform these actions and will deplete the
                                               cost amount from your bank. 
                                            - There are 3 types of energy ('water', 'fire', and 'earth') and an "any" energy type. The 'any'
                                              energy type will work as a "reserve" energy type. It is only used if you do not have enough elemental 
                                              energy to perfrom a given action.
                                            - example-  If you have a monster that is a fire type, and you are attacking your opponent with an attack
                                              cost of 3 energy..... lets say you have only 1 'fire' energy and 3 'any' energies in your bank. The 
                                              attack will deplete the 1 'fire' energy and then deplete 2 'any' energies in order to perform the 
                                              attack.

***HEAL***
- You can heal a monster once per turn. If you choose to heal, it will add the amount of heal to your monsters HP and deplete the corresponding          energy from your bank.

***PLAY SPECIAL CARD***
- You can play two special cards per turn. When you play the "Special"card it will perform the action stated on the card.

***ATTACK***    
- Attacks opponents monster in play with the 'attack' amount. Depletes 'attack cost' of energy from opponents 'in play' monster HP. 
- Pay attention to the monster types you have in play. If your monster has an elemental advantage over the other monster, add 15 attack points when     attacking.
- If there is an unforeseen event occurring, and your monster shares the same elemental type of the event (and your opponents monster does not),
  Also add the event amount to the attack in progress.
  
  
  
 *** HOW TO WIN***
 - 3 ways to win the game.
 
                       - Achieve the predetermined number of knockouts before your opponent
                       
                       - Opponent runs out of cards to draw into their hand
                       
                       - Knockout the opponents monster card and they have no monster cards in their hand to put into play.
                       
                       
                       
                       
                       
                       
                                                                             
                                                                            
                                     
                                                                           
                                                                               

