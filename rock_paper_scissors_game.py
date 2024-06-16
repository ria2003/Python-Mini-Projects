import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk

class Game(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("520x520")
        self.title("Rock Paper Scissors")

        self.configure(bg='floral white')

        self.heading = tk.Label(self, font=("Cooper Black", 24, "italic"), text="Rock Paper Scissors", foreground="black", background="floral white")
        self.heading.pack(pady=(25,20))

        score_frame = tk.Frame(self, background="floral white")
        score_frame.pack(fill=tk.X)

        self.player_score = tk.Label(score_frame, font=("Arial", 12, 'bold'), text="Your Score:", foreground="red4", background="floral white")
        self.player_score.pack(side="left", expand=True, padx=(0,80))

        self.computer_score = tk.Label(score_frame, font=("Arial", 12, 'bold'), text="Computer Score:", foreground="red4", background="floral white")
        self.computer_score.pack(side="left", expand=True, padx=(80,0))

        score_count_frame = tk.Frame(self, background="floral white")
        score_count_frame.pack(fill=tk.X)
        score_count_frame.grid_columnconfigure(0, weight=1)

        self.player_score_value = 0
        self.computer_score_value = 0

        self.player_score_count = tk.Label(score_count_frame, font=("Arial", 14, "bold"), text=str(self.player_score_value), foreground="red4", background="floral white")
        self.player_score_count.grid(row=0, column=0,  pady=(0,15), sticky='ew')

        self.computer_score_count = tk.Label(score_count_frame, font=("Arial", 14, "bold"), text=str(self.computer_score_value), foreground="red4", background="floral white")
        self.computer_score_count.grid(row=0, column=1, pady=(0,15), sticky='ew', padx=(275,80))

        self.player_label = tk.Label(self, font=("Arial", 16), text="You", foreground="black", background="floral white")
        self.player_label.pack(pady=(0,10))

        icons_frame = tk.Frame(self, background="floral white")
        icons_frame.pack(fill=tk.X)

        self.img1 = Image.open(r'C:\Users\HP\Downloads\fist.png')
        self.image1 = self.img1.resize((45, 45))
        self.rock_img = ImageTk.PhotoImage(self.image1)
        self.rock_btn = ttk.Label(icons_frame, image=self.rock_img, background="floral white", cursor="hand2")
        self.rock_btn.pack(side='left', expand=True)
        self.rock_btn.bind("<Button-1>", lambda event: self.play("rock"))

        self.img2 = Image.open(r'C:\Users\HP\Downloads\paper.png')
        self.image2 = self.img2.resize((45, 45))
        self.paper_img = ImageTk.PhotoImage(self.image2)
        self.paper_btn = ttk.Label(icons_frame, image=self.paper_img, background="floral white", cursor="hand2")
        self.paper_btn.pack(side='left', expand=True)
        self.paper_btn.bind("<Button-1>", lambda event: self.play("paper"))

        self.img3 = Image.open(r'C:\Users\HP\Downloads\scissor.png')
        self.image3 = self.img3.resize((45, 45))
        self.scissor_img = ImageTk.PhotoImage(self.image3)
        self.scissor_btn = ttk.Label(icons_frame, image=self.scissor_img, background="floral white", cursor="hand2")
        self.scissor_btn.pack(side='left', expand=True)
        self.scissor_btn.bind("<Button-1>", lambda event: self.play("scissors"))

        self.computer_label = tk.Label(self, font=("Arial", 16), text="Computer", foreground="black", background="floral white")
        self.computer_label.pack(pady=(30,10))

        self.computer_choice_img = ttk.Label(self, background="floral white")
        self.computer_choice_img.pack(pady=(0,30))

        self.result = ttk.Label(self, background="floral white", font=("Arial", 12, "bold"))
        self.result.pack(padx=10)

        self.images = {
            "rock": self.rock_img,
            "paper": self.paper_img,
            "scissors": self.scissor_img
        }

        buttons_frame = tk.Frame(self, background="floral white")
        buttons_frame.pack(fill=tk.X)


        self.reset_button=tk.Button(buttons_frame, text="Reset", font=("Arial", 12, "bold"), foreground='white', background='maroon', bd=2, cursor="hand2")
        self.reset_button.pack(side='left', pady=(35,20), ipadx=35, ipady=3, padx=(30,0), expand=True)
        self.reset_button.bind("<Button-1>", self.reset_game)

        self.rules_button=tk.Button(buttons_frame, text="Rules", font=("Arial", 12, "bold"), foreground='white', background='maroon', bd=2, cursor="hand2")
        self.rules_button.pack(side='left', pady=(35,20), ipadx=35, ipady=3, padx=(0,30), expand=True)
        self.rules_button.bind("<Button-1>", self.display_rules)

    def play(self, player_choice):
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        win_conditions = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if win_conditions[player_choice] == computer_choice:
            self.player_score_value += 10
            self.result.config(text=f"You chose {player_choice} and Computer chose {computer_choice}. You Win!")

        elif win_conditions[computer_choice] == player_choice:
            self.computer_score_value += 10
            self.result.config(text=f"You chose {player_choice} and Computer chose {computer_choice}. Computer Wins!")
        else:
            self.result.config(text=f"You chose {player_choice} and Computer chose {computer_choice}. It's a tie!")

        self.player_score_count.config(text=str(self.player_score_value))
        self.computer_score_count.config(text=str(self.computer_score_value))

        self.computer_choice_img.config(image=self.images[computer_choice])

    def reset_game(self, event):
        if self.reset_button:
            self.player_score_value=0
            self.computer_score_value=0
            self.player_score_count.config(text=str('0'))
            self.computer_score_count.config(text=str('0'))
            self.computer_choice_img.config(image="")
            self.result.config(text="")

    def display_rules(self, event):
        if self.rules_button:
            rules=tk.Toplevel(self)
            rules.title("Game Rules")
            rules.geometry('570x520')

            rules.configure(bg='firebrick4')

            rules_label=tk.Label(rules, text="Game Rules", font=("Cooper Black", 18, 'italic'), foreground="white", bg="firebrick4")
            rules_label.pack(pady=(20,15))

            rules_text = (
            "1. Objective: Defeat your opponent by choosing a weapon that beats their choice.\n\n"
            "2. Choices:\n"
            "   - Rock\n"
            "   - Paper\n"
            "   - Scissors\n\n"
            "3. Winning Conditions:\n"
            "   - Rock crushes Scissors.\n"
            "   - Scissors cuts Paper.\n"
            "   - Paper covers Rock.\n\n"
            "4. Scoring:\n"
            "   - Win: +10 points\n"
            "   - Tie: 0 points\n\n"
            "5. Gameplay:\n"
            "   - Click a button to choose Rock, Paper, or Scissors.\n"
            "   - The computer randomly chooses its weapon.\n"
            "   - The result and updated scores are displayed.\n\n"
            "6. Reset:\n"
            "   - Click 'Reset' to set both scores to 0.\n\n"
            "                                             Have Fun. Enjoy the game!\n"
        )

        rules_message = tk.Label(rules, text=rules_text, font=("Arial", 11), foreground="white", bg="firebrick4", justify=tk.LEFT)
        rules_message.pack(padx=10, pady=(0,10))

if __name__ == '__main__':
    app = Game()
    app.mainloop()
