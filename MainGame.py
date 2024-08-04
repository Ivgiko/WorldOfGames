import Live
from CurrencyRouletteGame import play as roulette
from MemoryGame import play as memory
from GuessGame import play as guess

print(Live.welcome("Guy"))
game, difficulty = Live.load_game()
if game == 1:
    print("You won!" if memory(difficulty) is True else "You lost")
if game == 2:
    print("You won!" if guess(difficulty) is True else "You lost")
if game == 3:
    print("You won!" if roulette(difficulty) is True else "You lost")

