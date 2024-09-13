
def welcome(name):
    return (f"Hello {name} and welcome to the World of Games (WoG). \n"
            f"Here you can find many cool games to play.")


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
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



# from flask import Flask, render_template, request, session
#
# app = Flask(__name__)
# app.secret_key = 'your_secret_key'
#
#
# # Function to welcome the user
# def welcome(name):
#     return (f"Hello {name} and welcome to the World of Games (WoG). \n"
#             f"Here you can find many cool games to play.")
#
#
# # Route for the welcome page
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# # Route for loading the game selection
# @app.route('/load_game', methods=['POST'])
# def load_game():
#     name = request.form['name']
#     message = welcome(name)
#     return render_template('load_game.html', message=message)
#
#
# # Route for handling the game and difficulty selection
# @app.route('/play_game', methods=['POST'])
# def play_game():
#     game = int(request.form['game'])
#     difficulty = int(request.form['difficulty'])
#
#     if 1 <= game <= 3 and 1 <= difficulty <= 5:
#         # Store them in session
#         session['game'] = game
#         session['difficulty'] = difficulty
#         return "Parameters stored successfully!"
#     else:
#         return "Invalid game or difficulty selection. Please try again."
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

