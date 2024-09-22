from flask import Flask, request, jsonify
import random
import sys
from shared.Score import add_score

app = Flask(__name__)

# Game logic
def generate_number(difficulty):
    """Generate a random number between 1 and the difficulty level."""
    return random.randint(1, difficulty)

def compare_results(user_guess, difficulty):
    """Compare the user's guess with the generated number."""
    generated_number = generate_number(difficulty)

    if user_guess == generated_number:
        print(f"User guessed correctly! Adding score for difficulty: {difficulty}")
        sys.stdout.flush()  # Ensure the print shows up in logs
        add_score(difficulty)  # Add the score if the guess is correct
        return True, generated_number
    else:
        print(f"User guessed {user_guess}, but the correct number was {generated_number}.")
        sys.stdout.flush()
        return False, generated_number

# Flask routes

# Play the game via JSON request
@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    difficulty = data.get('difficulty')
    user_guess = data.get('user_guess')

    if difficulty is None or user_guess is None:
        return jsonify({"error": "Missing required data"}), 400

    result, generated_number = compare_results(user_guess, difficulty)

    return jsonify({
        "result": result,
        "generated_number": generated_number
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
