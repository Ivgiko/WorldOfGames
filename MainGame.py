from flask import Flask, render_template, request, redirect, url_for, session
import Live
import CurrencyRouletteGame
import MemoryGame
import GuessGame
import Score

app = Flask(__name__, template_folder='templates/')
app.secret_key = 'my_super_secret_key_123'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['name']
    welcome_message = Live.welcome(name)
    return render_template('load_game.html', welcome_message=welcome_message)


@app.route('/load_game', methods=['POST'])
def load_game():
    game = int(request.form['game'])
    difficulty = int(request.form['difficulty'])

    # Redirect to game routes based on game selection
    if game == 1:
        return redirect(url_for('memory_game', difficulty=difficulty))
    elif game == 2:
        return redirect(url_for('guess_game', difficulty=difficulty))
    elif game == 3:
        return redirect(url_for('roulette_game', difficulty=difficulty))
    else:
        return "Invalid game selection"


@app.route('/memory/<int:difficulty>', methods=['GET'])
def memory_game(difficulty):
    # Generate the random sequence and store it in the session
    rand_list = MemoryGame.generate_sequence(difficulty)
    session['rand_list'] = rand_list

    # Show the sequence and then redirect to the input form after a delay
    return render_template('show_sequence.html', rand_list=rand_list, difficulty=difficulty)


@app.route('/memory_input/<int:difficulty>', methods=['GET', 'POST'])
def memory_input(difficulty):
    if request.method == 'POST':
        user_guesses = []
        error = None

        # Collect guesses and validate input
        for i in range(difficulty):
            guess = request.form.get(f'guess{i + 1}')
            try:
                guess = int(guess)
                if 1 <= guess <= 101:
                    user_guesses.append(guess)
                else:
                    error = "Each number must be between 1 and 101."
                    break
            except ValueError:
                error = "Invalid input! Please enter only numbers."
                break

        # If there's an error, re-render the form with the error message
        if error:
            return render_template('memory_form.html', difficulty=difficulty, error=error)

        # Retrieve the generated sequence from session
        rand_list = session.get('rand_list', [])

        # Compare the user's guesses with the generated sequence
        result = MemoryGame.is_list_equal(rand_list, user_guesses)

        if result:
            return render_template('game_result.html', result="You won!")
        else:
            return render_template('game_result.html', result="You lost!")

    # If the method is GET, just render the form
    return render_template('memory_form.html', difficulty=difficulty)


@app.route('/guess/<int:difficulty>', methods=['GET', 'POST'])
def guess_game(difficulty):
    if request.method == 'POST':
        # Get user's guess from the form
        user_guess = int(request.form['guess'])

        # Retrieve the generated number from the session
        generated_number = session.get('generated_number')

        # Compare the guess with the generated number
        if user_guess == generated_number:
            return render_template('game_result.html', result="You won!")
        else:
            return render_template('game_result.html', result=f"You lost! The correct number was {generated_number}.")
    else:
        # Generate a random number and store it in the session
        generated_number = GuessGame.generate_number(difficulty)
        session['generated_number'] = generated_number

        # Render a form to collect user's guess
        return render_template('guess_form.html', difficulty=difficulty)


@app.route('/roulette/<int:difficulty>', methods=['GET', 'POST'])
def roulette_game(difficulty):
    if request.method == 'POST':
        # Get the user's guess from the form
        user_guess = float(request.form['guess'])

        # Retrieve the generated number (USD amount) from the session
        usd_amount = session.get('usd_amount')

        # Calculate the interval using the get_money_interval function
        interval = CurrencyRouletteGame.get_money_interval(difficulty, usd_amount)

        # Check if the guess falls within the interval
        if interval[0] <= user_guess <= interval[1]:
            return render_template('game_result.html', result="You won!")
        else:
            return render_template('game_result.html', result=f"You lost! The correct interval was {interval}.")
    else:
        # Generate a random amount in USD
        usd_amount = CurrencyRouletteGame.generate_number()
        session['usd_amount'] = usd_amount

        # Prompt user to guess the value in ILS
        return render_template('roulette_form.html', usd_amount=usd_amount)


@app.route("/score")
def score_server():
    file = open('Utils.py', "r")
    read = file.read()
    for line in read.splitlines():
        if 'SCORES_FILE_NAME' in line:
            scoresfile = line.split('=',1)[1]
    try:
        with open(scoresfile, 'r') as file:
            read = file.read()
            return render_template('score.html', SCORE=read)
            file.close()
    except FileNotFoundError:
        return render_template('error.html', ERROR="No Score file found")


if __name__ == '__main__':
    app.run(debug=True)
