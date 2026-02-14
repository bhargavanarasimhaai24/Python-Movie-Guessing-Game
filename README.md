🎬 Tkinter Movie Poster Guessing Game

An interactive and strategy-based movie guessing game built using Python, Tkinter, and Pillow (PIL).

This project combines GUI development, image processing, and game logic design to create an engaging experience where players guess movies from blurred posters with optional strategic hints.



🚀 Project Overview

This game challenges players to identify a movie title using:

* A blurred movie poster

* Optional dialogue hints

* A limited number of lives

* A countdown timer

* A point-based scoring system

The player must strategically decide when to reveal hints, as each hint reduces their total score.



🧠 Core Features

🎬 Blurred Poster Reveal System

* Posters start with Gaussian blur

* Blur reduces only when the player uses a hint

* Implemented using Pillow’s image filtering

💬 Dialogue Hint Mechanism

* Reveal iconic dialogue at a point cost

* Encourages strategic decision-making

🎯 Multiple Difficulty Levels

* Easy / Medium / Hard

* Adjusts:

  Timer duration

  Number of lives

  Initial blur intensity

⏳ Countdown Timer

* Real-time timer using Tkinter’s after() method

* Game ends when time runs out

❤️ Lives System

* Limited incorrect guesses allowed

* Visual heart-based life display

💰 Dynamic Scoring System

* +5 points for correct letter

* +20 points for correct movie guess

* -2 points for poster reveal

* -3 points for dialogue reveal

* Prevents negative scoring

🖼️ Image Processing Integration

* Gaussian blur manipulation using Pillow

* Dynamic poster update rendering
  


🏗️ Technical Implementation

🔹 Technologies Used

* Python 3.x

* Tkinter (GUI Framework)

* Pillow (PIL) for image processing

🔹 Architecture Design

The project follows a modular and class-based design:

* Start Screen → Difficulty Selection

* GameGUI Class

  UI creation

  Game state management
  
  Timer logic
  
  Hint handling
  
  Score tracking
  
  Poster rendering

Game logic is cleanly separated into methods such as:

* create_ui()

* update_blanks()

* submit_guess()

* reveal_poster()

* reveal_dialogue()

* start_timer()

* end_game()



🎮 Gameplay Mechanics

* Player selects difficulty.

* A blurred movie poster is displayed.

* Player guesses:

  Single letters
  
  Or full movie title

* Player may:

  Reveal poster partially (-2 points)
  
  Reveal dialogue hint (-3 points)

* Game ends when:

  Movie is guessed correctly
  
  Lives reach zero
  
  Timer expires



📌 Design Thinking Behind the Game

This project demonstrates:

  * Event-driven programming
  
  * State management in GUI applications
  
  * Strategic user interaction design
  
  * Image manipulation in real-time
  
  * Responsive layout handling in Tkinter
  
The hint deduction system ensures the game is not purely guess-based but decision-driven.


📂 Project Structure

├── main.py
├── posters/
│   ├── movie1.jpg
│   ├── movie2.jpg
├── game.py
├── movies_data.py
└── README.md


▶️ How to Run

Clone the repository: git clone https://github.com/your-username/repo-name.git
Install dependencies: pip install pillow
Run: python main.py


🌟 Future Improvements

* Add leaderboard system

* Add sound effects

* Add animations for blur transitions

* Add more movie datasets (JSON-based)

* Add multiplayer mode

* Improve UI styling



📈 Skills Demonstrated

* Object-Oriented Programming

* GUI Application Development

* Image Processing

* Game Logic Design

* Event Handling

* State Management

* User Interaction Design
