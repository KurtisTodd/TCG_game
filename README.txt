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
                                     or    Attack                 x1        
      
- You may choose these options in any order you wish with but one stipulation. When and if you attack, (not including playing an 'attack' card)
  you are forfeiting the rest of your turn.
  
- Pay attention to the monster types you have in play. If your monster has an elemental advantage over the other monster, add 15 attack points when     attacking.
                                                                             
                                                                            
                                     
                                                                           
                                                                               

- If you attack, your turn is over.
- If you play an energy card, the amount of that energy card is added to energy in play. You can have an infinite amount of energy in play, but every     time you attack or heal it costs energy, and will deplete the corresponding "cost amount".
- 
