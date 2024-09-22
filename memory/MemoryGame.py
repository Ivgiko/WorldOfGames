from flask import Flask, request, jsonify, session
import random
import sys
from shared.Score import add_score

app = Flask(__name__)
app.secret_key = 'super_secret_key_memory_game'  # Needed for session handling

# Generate sequence based on difficulty
def generate_sequence(difficulty):
    sequence = random.sample(range(1, 101), difficulty)
    print(f"Generated sequence for difficulty {difficulty}: {sequence}")
    sys.stdout.flush()
    return sequence

# Play the game (start or continue)
@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    difficulty = data.get("difficulty")
    if difficulty is None:
        return jsonify({"error": "Difficulty not provided"}), 400

    rand_list = generate_sequence(difficulty)
    session['rand_list'] = rand_list  # Store the sequence in session for comparison later
    return jsonify({"sequence": rand_list})

# Handle user's guesses
@app.route('/compare', methods=['POST'])
def memory_input():
    data = request.get_json()
    difficulty = data.get("difficulty")
    user_guesses = data.get("user_list")
    rand_list = data.get("rand_list")

    if difficulty is None or user_guesses is None or rand_list is None:
        return jsonify({"error": "Missing required data"}), 400

    print(f"User's guesses: {user_guesses}")
    sys.stdout.flush()

    # Compare user's guesses to the generated sequence
    result = is_list_equal(rand_list, user_guesses, difficulty)
    return jsonify({"result": result})

# Compare the user's guesses to the generated sequence
def is_list_equal(rand_list, guess, difficulty):
    print(f"Comparing user guesses: {guess} with generated sequence: {rand_list}")
    sys.stdout.flush()
    if sorted(guess) == sorted(rand_list):
        print(f"User guessed correctly, adding score for difficulty {difficulty}")
        sys.stdout.flush()
        add_score(difficulty)  # Add the score if correct
        return True
    else:
        print("User guessed incorrectly.")
        sys.stdout.flush()
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
