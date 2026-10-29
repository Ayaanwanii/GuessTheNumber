# 🎯 Guess the Number

This is a small web game built with **Python** and **Streamlit**. The computer secretly chooses a number from **1 to 100**. The player keeps guessing until they find it.

The project is deliberately small and uses clear names, so it is a good introduction to Python programming and simple web apps.

## What the player sees

The page has:

- A title and instructions.
- A number box where the player enters a guess from 1 to 100.
- A **Check my guess** button.
- A message saying whether the guess is too high, too low, or correct.
- An attempt counter.
- A **Start a new game** button in the sidebar.

## What you need

- Python 3 installed.
- A terminal (Terminal on macOS, Command Prompt or PowerShell on Windows).
- An internet connection the first time you install Streamlit.

## How to run the project

1. Open a terminal in the project folder.
2. Install the required library:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the game:

   ```bash
   streamlit run app.py
   ```

4. Streamlit will open the game in a browser. If it does not open automatically, go to the address printed in the terminal, usually `http://localhost:8501`.

5. To stop the game server, return to the terminal and press `Ctrl + C`.

## Files in this project

| File | What it does |
| --- | --- |
| `app.py` | The complete Python program for the game. |
| `cli_game.py` | A basic version of the game that runs in a terminal. |
| `requirements.txt` | Lists Streamlit, the library needed to run the app. |
| `README.md` | Explains the project and the code. |
| `CLI_README.md` | Explains the command-line version and compares both programs. |

## The big idea

```text
Start game
    ↓
Computer chooses a random number from 1 to 100
    ↓
Player enters a guess and clicks the button
    ↓
Is the guess smaller, larger, or equal to the secret number?
    ↓
Show a hint, or celebrate if the answer is correct
```

## Code walkthrough

Open `app.py` and follow these sections from top to bottom.

### 1. Importing libraries

```python
import random
import streamlit as st
```

A **library** is ready-made code written by other programmers.

- `random` lets Python select a random number.
- `streamlit` helps us create buttons, text, number boxes, and other parts of a webpage.
- `as st` gives Streamlit a short name. Writing `st.button(...)` is easier than writing `streamlit.button(...)`.

### 2. Setting up the page

```python
st.set_page_config(page_title="Guess the Number", page_icon="🎯")
```

This changes the browser tab title and adds an emoji icon to the tab.

### 3. Creating a function for a new game

```python
def start_new_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_won = False
    st.session_state.message = "I picked a number from 1 to 100. Can you find it?"
```

A **function** is a named set of instructions that we can use again. This function starts a fresh game.

| Line | Meaning |
| --- | --- |
| `random.randint(1, 100)` | Chooses a whole number from 1 up to and including 100. |
| `secret_number` | Stores the number the player must guess. |
| `attempts = 0` | Resets the number of guesses made. |
| `game_won = False` | Says that the game has not been won yet. |
| `message` | Stores the message shown to the player. |

### 4. Remembering values with session state

```python
if "secret_number" not in st.session_state:
    start_new_game()
```

Streamlit runs `app.py` again after a player clicks a button. Without special memory, the secret number would change every time.

`st.session_state` is like a small backpack for this one player's game. It remembers information between button clicks. This `if` statement checks whether a game has been created already. If not, it calls `start_new_game()`.

### 5. Showing text and the New Game button

```python
st.title("🎯 Guess the Number")
st.write("Try to guess the secret number between **1 and 100**.")
```

- `st.title` displays a large heading.
- `st.write` displays normal text. The `**words**` marks make words bold.

The code inside `with st.sidebar:` puts items in the left sidebar. When the player clicks **Start a new game**, the program calls `start_new_game()` and refreshes the screen with `st.rerun()`.

### 6. Getting the player's guess

```python
guess = st.number_input(
    "Your guess",
    min_value=1,
    max_value=100,
    value=50,
    step=1,
)
```

`st.number_input` creates a number box.

- The result is saved in the variable named `guess`.
- `min_value=1` and `max_value=100` prevent guesses outside the game range.
- `value=50` is the starting number in the box.
- `step=1` means the small arrows change the value by one.

### 7. Checking the guess

```python
if st.button("Check my guess"):
    st.session_state.attempts += 1
```

`st.button` creates a button. The code inside this `if` block runs only when the player clicks it.

`+= 1` means “add 1 to the current value.” Therefore each click increases the attempt counter by one.

### 8. Comparing numbers

```python
if guess < st.session_state.secret_number:
    # Too low
elif guess > st.session_state.secret_number:
    # Too high
else:
    # Correct
```

This is an **if / elif / else** decision.

| Operator | Meaning | Example |
| --- | --- | --- |
| `<` | smaller than | `4 < 9` is true |
| `>` | larger than | `10 > 3` is true |
| `==` | equal to | `7 == 7` is true |

The program first checks if the guess is too low. If it is not, it checks if the guess is too high. If neither is true, it must be exactly correct, so the `else` section runs.

When the answer is correct, the program also changes `game_won` to `True`. This disables the guessing controls and lets the program show a celebration.

### 9. Showing feedback

```python
if st.session_state.game_won:
    st.success(st.session_state.message)
else:
    st.info(st.session_state.message)
```

- `st.info` displays a blue information box for normal hints.
- `st.success` displays a green success box when the player wins.
- `st.write(f"**Attempts:** {st.session_state.attempts}")` uses an **f-string** to put the current attempt count inside a sentence.

## Important Python ideas used

| Idea | Example in this project | Why it helps |
| --- | --- | --- |
| Variables | `guess`, `attempts` | Store information. |
| Functions | `start_new_game()` | Reuse a group of instructions. |
| Conditions | `if`, `elif`, `else` | Let the code make decisions. |
| Comparison operators | `<` and `>` | Compare the guessed number with the secret number. |
| Boolean values | `True` and `False` | Store yes/no information, such as whether the game is won. |
| Libraries | `random`, `streamlit` | Add useful features without writing everything yourself. |

## Try changing the game

Make one change at a time, save `app.py`, and see the webpage refresh.

### Change the number range

To use numbers from 1 to 50, change both occurrences of `100` in these parts:

```python
random.randint(1, 100)
max_value=100
```

Also update the text shown to the player so that the instructions match the game.

### Make an easier game

Change the range to 1 to 20. Why will this usually take fewer guesses?

### Add a limit on guesses

Before the player makes another guess, check whether `attempts` has reached 7. If it has, show the secret number and ask them to start again.

### Keep a guess history

Create a list in `start_new_game()` named `guesses`, then add each new guess to it. Finally, display the list below the attempt count.

### Add difficulty levels

Use `st.selectbox` to let the player choose easy (1–20), medium (1–50), or hard (1–100).

## Questions to check your understanding

1. Why does the game need the `random` library?
2. What would happen if `secret_number` were created again every time a button was clicked?
3. What is the difference between `=` and `==` in Python?
4. Why does the code use `elif` for the “too high” check?
5. What does `st.session_state` remember?
6. Where would you change the game to make the biggest number 200?

## Troubleshooting

| Problem | What to try |
| --- | --- |
| `streamlit: command not found` | Run `python3 -m pip install -r requirements.txt`, then run `python3 -m streamlit run app.py`. |
| The browser page does not open | Copy the local URL printed in the terminal and paste it into a browser. |
| `ModuleNotFoundError: No module named 'streamlit'` | Install the dependencies again with `pip install -r requirements.txt`. |
| The app is still running | Go to the terminal and press `Ctrl + C`. |

Have fun changing the game and seeing what each change does!
