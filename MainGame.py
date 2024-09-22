import random
import requests
from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine, text, Column, Integer
from sqlalchemy.orm import declarative_base
from alembic.config import Config
from alembic import command
import os

app = Flask(__name__, template_folder='templates/')
app.secret_key = 'my_super_secret_key_123'

# Database setup
DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://user:userpassword@db:3306/game_scores')
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define the UserScore model with score as the primary key
class UserScore(Base):
    __tablename__ = 'users_scores'
    score = Column(Integer, primary_key=True, nullable=False)

# Function to apply Alembic migrations
def run_alembic_migrations():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)
    command.upgrade(alembic_cfg, "head")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['name']
    welcome_message = f"Hello {name}, welcome to the World of Games!"
    return render_template('load_game.html', welcome_message=welcome_message)

@app.route('/load_game', methods=['POST'])
def load_game():
    game = int(request.form['game'])
    difficulty = int(request.form['difficulty'])

    if game == 1:
        return redirect(url_for('memory_game', difficulty=difficulty))
    elif game == 2:
        return redirect(url_for('guess_game', difficulty=difficulty))
    elif game == 3:
        return redirect(url_for('roulette_game', difficulty=difficulty))
    else:
        return "Invalid game selection"

# Memory Game microservice call
@app.route('/memory/<int:difficulty>', methods=['GET'])
def memory_game(difficulty):
    try:
        response = requests.post(f'http://memory:5001/play', json={"difficulty": difficulty})
        response.raise_for_status()
        rand_list = response.json()['sequence']
        session['rand_list'] = rand_list
        return render_template('show_sequence.html', rand_list=rand_list, difficulty=difficulty)
    except Exception as e:
        return str(e), 500

@app.route('/memory_form/<int:difficulty>', methods=['GET'])
def memory_form(difficulty):
    rand_list = session.get('rand_list', [])
    return render_template('memory_form.html', difficulty=difficulty, rand_list=rand_list)

@app.route('/memory_input/<int:difficulty>', methods=['POST'])
def memory_input(difficulty):
    user_guesses = [int(request.form.get(f'guess{i + 1}')) for i in range(difficulty)]
    rand_list = session.get('rand_list', [])
    try:
        response = requests.post(f'http://memory:5001/compare', json={"difficulty": difficulty, "rand_list": rand_list, "user_list": user_guesses})
        response.raise_for_status()
        result = response.json()['result']
        if result:
            return render_template('game_result.html', result="You won!")
        else:
            return render_template('game_result.html', result="You lost!")
    except Exception as e:
        return str(e), 500

# Guess Game microservice call
@app.route('/guess/<int:difficulty>', methods=['GET', 'POST'])
def guess_game(difficulty):
    if request.method == 'POST':
        user_guess = int(request.form['guess'])
        try:
            response = requests.post(f'http://guess:5002/play', json={"difficulty": difficulty, "user_guess": user_guess})
            response.raise_for_status()
            result = response.json()['result']
            if result:
                return render_template('game_result.html', result="You won!")
            else:
                return render_template('game_result.html', result=f"You lost! The correct number was {response.json()['generated_number']}.")
        except Exception as e:
            return str(e), 500
    else:
        return render_template('guess_form.html', difficulty=difficulty)

# Roulette Game microservice call
@app.route('/roulette/<int:difficulty>', methods=['GET', 'POST'])
def roulette_game(difficulty):
    if request.method == 'POST':
        user_guess = float(request.form['guess'])
        try:
            response = requests.post(f'http://roulette:5003/play', json={"difficulty": difficulty, "user_guess": user_guess})
            response.raise_for_status()
            result = response.json()['result']
            if result:
                return render_template('game_result.html', result="You won!")
            else:
                interval = response.json()['interval']
                return render_template('game_result.html', result=f"You lost! The correct interval was {interval}.")
        except Exception as e:
            return str(e), 500
    else:
        return render_template('roulette_form.html', difficulty=difficulty)

@app.route("/score")
def score_server():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT score FROM users_scores"))
            score = result.scalar()

            # If no scores are found, show "Your score is 0"
            if score is None:
                score = 0

            return render_template('score.html', SCORE=score)

    except Exception as e:
        return render_template('error.html', ERROR=str(e))


if __name__ == "__main__":
    run_alembic_migrations()
    app.run(host='0.0.0.0', port=5000)
