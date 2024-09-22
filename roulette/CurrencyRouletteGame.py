from flask import Flask, request, jsonify, render_template
from forex_python.converter import CurrencyRates
import random
import sys
from shared.Score import add_score

app = Flask(__name__)

def get_money_interval(difficulty, t):
    """Get the money interval based on difficulty and converted rate."""
    c = CurrencyRates()
    try:
        # Attempt to convert USD to ILS using the forex-python API
        rate = c.convert('USD', 'ILS', t)
        print(f"Fetched currency rate: 1 USD = {rate} ILS")  # Debugging log
    except Exception as e:
        print(f"Failed to fetch currency rate, using fallback. Error: {e}")
        sys.stdout.flush()
        rate = t * 3.5  # Fallback conversion rate if API fails
    interval = (rate - (5 - difficulty), rate + (5 - difficulty))
    print(f"Calculated money interval: {interval}")  # Debugging log
    return interval

def generate_number():
    """Generate a random number between 1 and 100."""
    t = random.randint(1, 100)
    print(f"Generated USD amount: {t}")  # Debugging log
    return t

# Play the game via JSON request
@app.route('/play', methods=['POST'])
def play():
    """Main game logic for currency roulette."""
    data = request.get_json()

    # Validate input
    difficulty = data.get('difficulty')
    user_guess = data.get('user_guess')

    if difficulty is None or user_guess is None:
        return jsonify({"error": "Missing required data"}), 400

    try:
        user_guess = float(user_guess)
    except ValueError:
        return jsonify({"error": "Invalid user_guess, must be a number"}), 400

    # Generate random USD amount
    t = generate_number()

    # Calculate the money interval
    interval = get_money_interval(difficulty, t)

    # Check if the user's guess is within the interval
    if interval[0] <= user_guess <= interval[1]:
        add_score(difficulty)  # Add score if the guess is correct
        result = True
    else:
        result = False

    print(f"Returning result: {result}, USD amount: {t}, Interval: {interval}")  # Debugging log

    return jsonify({
        'result': result,
        'generated_number': t,
        'interval': interval
    })

# Route to show the question
@app.route('/ask_question/<int:difficulty>', methods=['GET'])
def ask_question(difficulty):
    """Render the question asking how much USD is in ILS."""
    t = generate_number()  # Generate the number again
    print(f"Passing USD amount: {t} to the ask_question template")  # Debugging log
    # Pass difficulty too, to match what you get in the game
    return render_template('ask_question.html', usd_amount=t, difficulty=difficulty)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
