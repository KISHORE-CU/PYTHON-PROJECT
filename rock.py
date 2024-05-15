import tkinter as tk
import random

def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create the player's choice buttons
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=1, columnspan=3, padx=5, pady=10)

root.mainloop()
