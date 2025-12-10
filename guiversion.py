import tkinter as tk
import random

# Choice mapping
choices = {1: "Snake", -1: "Water", 0: "Gun"}

# Game logic
def determine_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 1 and computer == -1) or \
         (user == -1 and computer == 0) or \
         (user == 0 and computer == 1):
        return "You win!"
    else:
        return "You lose!"

# Function called when user clicks a button
def play(user_choice):
    user = user_choice
    computer = random.choice([1, -1, 0])
    result = determine_winner(user, computer)

    result_label.config(text=f"Your choice: {choices[user]}\nComputer's choice: {choices[computer]}\n{result}")

# Create the GUI window
window = tk.Tk()
window.title("Snake Water Gun Game")
window.geometry("350x300")
window.configure(bg="#eef")

# Title Label
title_label = tk.Label(window, text="Snake Water Gun", font=("Arial", 20, "bold"), bg="#eef", fg="#333")
title_label.pack(pady=10)

# Buttons for choices
btn_frame = tk.Frame(window, bg="#eef")
btn_frame.pack(pady=10)

snake_btn = tk.Button(btn_frame, text="Snake 🐍", width=10, command=lambda: play(1))
snake_btn.grid(row=0, column=0, padx=5)

water_btn = tk.Button(btn_frame, text="Water 💧", width=10, command=lambda: play(-1))
water_btn.grid(row=0, column=1, padx=5)

gun_btn = tk.Button(btn_frame, text="Gun 🔫", width=10, command=lambda: play(0))
gun_btn.grid(row=0, column=2, padx=5)

# Result display
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#eef", fg="#111")
result_label.pack(pady=20)

# Run the window
window.mainloop()
