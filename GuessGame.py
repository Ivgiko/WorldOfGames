import random
def generate_number(difficulty):
    return random.randint(1, difficulty)
def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Enter number between 1 and {difficulty} :"))
            if 1 <= guess <= difficulty: break
            else: continue
        except BaseException as e: continue
    return guess
def compare_results(difficulty):
    return True if get_guess_from_user(difficulty) == generate_number(difficulty) else False
def play(difficulty):
    return compare_results(difficulty)

