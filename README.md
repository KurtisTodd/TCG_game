# TCG_game
A python 2-player TCG game just for experimentation, learning, and fun.

There are 3 types of cards.
- Energy cards including up to 3 units of energy ('class'= 'energy') attributes = (.type = 'water', 'fire', 'earth') (amount = 1 , 2 , or 3)
- Monster cards ('class' = 'monster') attributes= name, hp, attack, attack cost, heal amount, heal cost, type ='water', 'fire', 'earth' 
- Special cards ('class' = 'special') attributes = amount(.type = "draw special cards", "draw monster cards", "attack", "heal", "draw", etc)  


Beginning of game.
- Each players deck are filled with random cards, but each deck has the same number of monsters, energy, and special cards.
- Each player draws 6 random cards from there deck and into their hand as well as at least 1 monster card. (7 total)
- each player gets to see their hand and choose which monster to "put into play." Each player must have one monster in play during their turn. If a       monster is "knocked out," the player must choose a monster from their hand and put it in play. If a player's monster is knocked out and has no monster   to put into play, the opponent wins.
- During each turn, player can choose to Retreat, Heal, Play energy, Play a special card, Attack, or skip thier turn.
- During each turn you can:
                            -Retreat once
                            -Heal once
                            -Play 2 special cards
                            -Play one energy card
                            -Attack once.

- If you attack, your turn is over.
- If you play an energy card, the amount of that energy card is added to energy in play. You can have an infinite amount of energy in play, but every     time you attack or heal it costs energy, and will deplete the corresponding "cost amount".
- 
