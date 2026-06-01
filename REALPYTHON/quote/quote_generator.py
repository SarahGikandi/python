#import tkinter as tk
import random

quotes = [
    "I DON'T HAVE TO BE ANYBODY BECAUSE AM ALREADY ME.",
    "PLANS ARE LIKE MEN, IT'S BEST TO AVOID THE COMPLICATED ONES.",
    "BELIEVE YOU CAN AND YOU ARE HALFWAY THERE.",
    "NOTHING BEHIND ME EVERYTHING AHEAD OF ME AS IS EVER SO ON THE ROAD.",
    "EVERY DAY IS A SECOND CHANCE.",
    "STAY POSITIVE, WORK HARD, MAKE IT HAPPEN.",
    "DREAM BIG AND DARE TO FAIL."
]


print("Hi Jedz😎, Here is Your Motivation quote for Today🥰: ")
print(random.choice(quotes))

input("\n\nPress ENTER to close this window...")

# def main():
#     root = tk.Tk()
#     root.title("Morning Quote")
#     root.attributes("-fullscreen", True)
#     root.configure(bg='#f0f8ff')
#     #quote_text = random.choice(quotes)
#     label = tk.Label(root, text=random.choice(quotes), font=("Segoe UI", 40), fg="#333", bg="#f08ff", wraplength=1000, justify="center")
#     label.pack(expand=True)
#
#     root.bind("<Escape>", lambda e: root.destroy())
#     #root.bind("<Button>", lambda e: root.destroy())
#
#     root.mainloop()
#     input("Press Enter to exit...")
#
# if "_name_" == "_main_":
#     main()