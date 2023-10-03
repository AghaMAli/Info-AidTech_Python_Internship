import random
import tkinter as tk

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def roll_dice_and_update_label():
    num_dice = int(num_dice_entry.get())
    dice_results = roll_dice(num_dice)
    result_label.config(text=f"Dice Results: {dice_results}")

def quit_app():
    root.destroy()

root = tk.Tk()
root.title(" IAT Dice Rolling App")

welcome_label = tk.Label(root, text="Welcome to the IAT Dice Rolling App!")
welcome_label.pack(pady=10)

num_dice_label = tk.Label(root, text="Enter the number of dice to roll:")
num_dice_label.pack()

num_dice_entry = tk.Entry(root)
num_dice_entry.pack()

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice_and_update_label)
roll_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(pady=10)

root.mainloop()