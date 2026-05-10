# 🐍💧🔫 Snake Water Gun Game

A Python implementation of the classic **Snake Water Gun** game (similar to Rock Paper Scissors), available in two versions: a command-line interface and a graphical user interface built with Tkinter.

---

## 🎮 Game Rules

| Choice | Beats |
|--------|-------|
| 🐍 Snake | 💧 Water (snake drinks water) |
| 💧 Water | 🔫 Gun (water douses gun) |
| 🔫 Gun | 🐍 Snake (gun shoots snake) |

Internally, choices are mapped to integers:
- `1` → Snake
- `-1` → Water
- `0` → Gun

---

## 📁 Project Structure

```
snake-water-gun/
│
├── main.py       # Command-line version
└── Gui.py        # Graphical user interface version
```

---

## 🖥️ Versions

### 1. Command-Line Version (`main.py`)

A simple terminal-based game. The player types their choice, and the computer picks randomly.

**How to run:**
```bash
python main.py
```

**Example session:**
```
WELCOME TO SNAKE WATER GUN GAME
Enter your choice (s for snake, w for water, g for gun): s
You chose : Snake
Computer chose: Water
You win!
```

**Input options:**
| Input | Choice |
|-------|--------|
| `s`   | Snake  |
| `w`   | Water  |
| `g`   | Gun    |

---

### 2. GUI Version (`Gui.py`)

A graphical version built with Python's built-in `tkinter` library. Click a button to make your choice and see the result instantly.

**How to run:**
```bash
python Gui.py
```

**Features:**
- Clean windowed interface (350×300)
- Three clickable buttons: Snake 🐍, Water 💧, Gun 🔫
- Displays both player and computer choices
- Shows result (Win / Lose / Draw) after each round

---

## ⚙️ Requirements

- Python 3.x
- `tkinter` (included in the Python standard library — no installation needed)
- No external packages required

---

## 🚀 Getting Started

1. **Clone or download** this repository.
2. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
3. Run either version:
   ```bash
   python main.py     # CLI
   python Gui.py      # GUI
   ```

---

## 📌 Notes

- The computer's choice is always random.
- The CLI version includes input validation — invalid entries prompt the user to try again.
- Both versions share the same core game logic.

