import random
import tkinter as tk
import tkinter.messagebox as msgbox
def generate_sequence(difficulty):
    return random.sample(range(1, 101), difficulty)
def showMessage(message, timeout=1000):
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    root.after(timeout, root.destroy)
    msgbox.showinfo('Memorise the numbers!', message, parent=root)
    root.mainloop()

def get_list_from_user(difficulty):
    user_list = []
    print(f"Enter {difficulty} numbers between 1 and 101 separated by enter:")
    for i in range(difficulty):
        while True:
            try:
                guess = int(input())
                if 1 <= guess <= 101:
                    user_list.append(guess)
                    break
                else: print("Enter number between 1 and 101")
            except BaseException as e: print("Enter number between 1 and 101")
    return user_list
def is_list_equal(randList, guess):
    return True if sorted(guess) == sorted(randList) else False
def play(difficulty):
    randList = generate_sequence(difficulty)
    showMessage(randList)
    guess = get_list_from_user(difficulty)
    return is_list_equal(randList, guess)


