def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play."

def load_game():
    print("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    while True:
        try:
            game = int(input())
            if 1 <= game <= 3:
                break
            else:
                print("Please enter game number between 1 and 3")
        except BaseException as e:
            print("Please enter game number between 1 and 3")
    print("Please choose game difficulty from 1 to 5:")
    while True:
        try:
            difficulty = int(input())
            if 1 <= difficulty <= 5:
                break
            else:
                print("Please choose game difficulty from 1 to 5:")
        except BaseException as e:
            print("Please choose game difficulty from 1 to 5:")
    return game, difficulty
