import tkinter as tk
import random
from PIL import Image, ImageTk, ImageFilter
import movies_data


class SelectionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Guessing Game")
        self.root.geometry("400x450")

        self.language = tk.StringVar(value="english")
        self.difficulty = tk.StringVar(value="Easy")

        tk.Label(root, text="🎬 Movie Guessing Game", font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(root, text="Select Language").pack()

        for lang in ["english", "hindi", "telugu", "kannada"]:
            tk.Radiobutton(root, text=lang.capitalize(),
                           variable=self.language,
                           value=lang).pack()

        tk.Label(root, text="Select Difficulty").pack(pady=10)

        for diff in ["Easy", "Medium", "Hard"]:
            tk.Radiobutton(root, text=diff,
                           variable=self.difficulty,
                           value=diff).pack()

        tk.Button(root, text="Start Game",
                  command=self.start_game,
                  bg="green", fg="white").pack(pady=20)

    def start_game(self):
        lang_dict = getattr(movies_data, self.language.get())
        movie_title = random.choice(list(lang_dict.keys()))
        movie_data = lang_dict[movie_title]

        self.root.destroy()
        new_root = tk.Tk()
        GameGUI(new_root, movie_title, movie_data, self.difficulty.get())
        new_root.mainloop()


class GameGUI:
    def __init__(self, root, title, data, difficulty):
        self.root = root
        self.root.title("Game Screen")
        self.root.geometry("1000x700")

        self.title_text = title.upper()
        self.poster_path = data["poster"]
        self.dialogue = data["dialogue"]

        self.guessed_letters = set()
        self.points = 0
        self.game_active = True
        self.dialogue_revealed = False

        settings = {
            "Easy": {"time": 120, "lives": 9, "blur": 15},
            "Medium": {"time": 90, "lives": 5, "blur": 25},
            "Hard": {"time": 60, "lives": 3, "blur": 35}
        }

        self.time_remaining = settings[difficulty]["time"]
        self.lives = settings[difficulty]["lives"]
        self.current_blur = settings[difficulty]["blur"]

        self.poster_reveal_cost = 2
        self.dialogue_cost = 3

        self.create_ui()
        self.update_blanks()
        self.update_stats()
        self.load_poster()
        self.start_timer()

    def create_ui(self):

        self.stats_label = tk.Label(self.root, font=("Arial", 12))
        self.stats_label.pack()

        self.poster_label = tk.Label(self.root)
        self.poster_label.pack(pady=10)

        self.blanks_label = tk.Label(
            self.root,
            font=("Courier", 26, "bold"),
            wraplength=900,  # prevents going outside window
            justify="center"
        )
        self.blanks_label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack()
        self.entry.bind("<Return>", lambda e: self.submit_guess())

        tk.Button(self.root, text="Submit",
                  command=self.submit_guess).pack(pady=10)

        self.message_label = tk.Label(self.root, font=("Arial", 12))
        self.message_label.pack(pady=10)

        # ---------------- HINT SECTION ---------------- #

        hint_frame = tk.Frame(self.root)
        hint_frame.place(relx=0.95, rely=0.95, anchor="se")

        tk.Label(hint_frame, text="Hints", font=("Arial", 12, "bold")).pack()

        tk.Button(hint_frame,
                  text="Reveal Poster (-2)",
                  command=self.reveal_poster).pack(pady=5)

        tk.Button(hint_frame,
                  text="Reveal Dialogue (-3)",
                  command=self.reveal_dialogue).pack(pady=5)

        self.dialogue_label = tk.Label(self.root, font=("Arial", 12),
                                       wraplength=600, fg="blue")
        self.dialogue_label.pack(pady=10)

    def load_poster(self):
        image = Image.open(self.poster_path)
        image = image.resize((300, 400))
        blurred = image.filter(ImageFilter.GaussianBlur(self.current_blur))
        self.tk_image = ImageTk.PhotoImage(blurred)
        self.poster_label.config(image=self.tk_image)

    def reveal_poster(self):
        if not self.game_active:
            return

        if self.points >= self.poster_reveal_cost and self.current_blur > 0:
            self.points -= self.poster_reveal_cost
            self.current_blur -= 5
            if self.current_blur < 0:
                self.current_blur = 0
            self.load_poster()
            self.message_label.config(text="Poster revealed slightly!")
        else:
            self.message_label.config(text="Not enough points or fully revealed!")

        self.update_stats()

    def reveal_dialogue(self):
        if not self.game_active:
            return

        if self.dialogue_revealed:
            self.message_label.config(text="Dialogue already revealed!")
            return

        if self.points >= self.dialogue_cost:
            self.points -= self.dialogue_cost
            self.dialogue_label.config(text=f"Dialogue Hint: \"{self.dialogue}\"")
            self.dialogue_revealed = True
            self.message_label.config(text="Dialogue revealed!")
        else:
            self.message_label.config(text="Not enough points!")

        self.update_stats()

    def update_blanks(self):
        display = ""
        for ch in self.title_text:
            if ch == " ":
                display += "   "
            elif ch in self.guessed_letters:
                display += ch + " "
            else:
                display += "_ "
        self.blanks_label.config(text=display)

    def update_stats(self):
        self.stats_label.config(
            text=f"Time: {self.time_remaining} | Lives: {self.lives}{'❤️'*self.lives} | Points: {self.points}"
        )

    def submit_guess(self):
        if not self.game_active:
            return

        guess = self.entry.get().strip().upper()
        self.entry.delete(0, tk.END)

        if len(guess) == 1:

            if guess in self.guessed_letters:
                self.message_label.config(text="Already guessed that letter!")
                return

            self.guessed_letters.add(guess)

            if guess in self.title_text:
                self.points += 5
                self.message_label.config(text="Correct letter! +5 points")
            else:
                self.lives -= 1
                self.message_label.config(text="Wrong letter! -1 life")

        else:
            if guess == self.title_text:
                self.points += 20
                self.current_blur = 0
                self.load_poster()
                self.end_game(True)
                return
            else:
                self.lives -= 1
                self.message_label.config(text="Wrong Guess! -1 life")

        self.update_blanks()
        self.update_stats()

        if "_" not in self.blanks_label.cget("text"):
            self.end_game(True)

        if self.lives <= 0:
            self.end_game(False)

    def start_timer(self):
        if self.time_remaining > 0 and self.game_active:
            self.time_remaining -= 1
            self.update_stats()
            self.root.after(1000, self.start_timer)
        elif self.time_remaining == 0:
            self.end_game(False)

    def end_game(self, won):
        self.game_active = False
        self.current_blur = 0
        self.load_poster()

        if won:
            self.message_label.config(text=f"🎉 You Won! Movie: {self.title_text}")
        else:
            self.message_label.config(text=f"Game Over! Movie was: {self.title_text}")
