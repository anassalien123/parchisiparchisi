import tkinter as tk
import random

# Define constants for the game
NUM_SQUARES = 29
GOAL = NUM_SQUARES - 1
MAX_PLAYERS = 4
PLAYER_NAMES = ["Player 1", "Player 2", "Player 3", "Player 4"]
SQUARE_SIZE = 40  # Size of each square on the grid

# Game state
players = []
current_turn = 0
player_positions = [0] * MAX_PLAYERS  # Start all players at the beginning (position 0)

# Initialize tkinter window
root = tk.Tk()
root.title("Parchisi Game")

# Create the canvas for the board
canvas = tk.Canvas(root, width=NUM_SQUARES * SQUARE_SIZE, height=5 * SQUARE_SIZE)
canvas.pack()

# Roll the dice
def roll_dice():
    return random.randint(1, 6)

# Create the board with squares
def draw_board():
    canvas.delete("all")
    for i in range(NUM_SQUARES):
        x1 = i * SQUARE_SIZE
        y1 = 0
        x2 = x1 + SQUARE_SIZE
        y2 = y1 + SQUARE_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
        canvas.create_text(x1 + SQUARE_SIZE / 2, y1 + SQUARE_SIZE / 2, text=str(i + 1), font=('Arial', 10))

# Create player tokens
def draw_players():
    for i, pos in enumerate(player_positions):
        if pos < NUM_SQUARES:
            x1 = pos * SQUARE_SIZE
            y1 = 0
            canvas.create_oval(x1 + 5, y1 + 5, x1 + SQUARE_SIZE - 5, y1 + SQUARE_SIZE - 5, fill=f"Player {i + 1}", tags=f"player{i}")

# Move player
def move_player(player_idx, roll):
    player_positions[player_idx] += roll
    if player_positions[player_idx] >= GOAL:
        player_positions[player_idx] = GOAL  # Ensure they don't pass the goal

# Update the game status label
def update_status():
    current_player = PLAYER_NAMES[current_turn]
    status_label.config(text=f"{current_player}'s turn\nRoll the dice!")

# Roll the dice and move the player
def take_turn():
    global current_turn
    roll = roll_dice()
    move_player(current_turn, roll)
    draw_board()
    draw_players()
    
    # Check if someone has won
    if player_positions[current_turn] == GOAL:
        winner = PLAYER_NAMES[current_turn]
        status_label.config(text=f"{winner} wins!")
    else:
        current_turn = (current_turn + 1) % MAX_PLAYERS
        update_status()

# Set up the UI elements
draw_board()
draw_players()

status_label = tk.Label(root, text="Player 1's turn\nRoll the dice!", font=('Arial', 14))
status_label.pack(pady=20)

roll_button = tk.Button(root, text="Roll Dice", font=('Arial', 12), command=take_turn)
roll_button.pack()

# Start the tkinter event loop
root.mainloop()
