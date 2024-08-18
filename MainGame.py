import Live
from CurrencyRouletteGame import play as roulette
from MemoryGame import play as memory
from GuessGame import play as guess
from Score import add_score as score

print(Live.welcome("Guy"))
game, difficulty = Live.load_game()
if game == 1:
    if memory(difficulty) is True:
        score(difficulty)
        print("You won!")
    else: print("You lost")
if game == 2:
    if guess(difficulty) is True:
        score(difficulty)
        print("You won!")
    else: print("You lost")
if game == 3:
    if roulette(difficulty) is True:
        score(difficulty)
        print("You won!")
    else: print("You lost")

