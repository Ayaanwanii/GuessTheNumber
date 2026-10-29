# Command-Line Guess the Number

`cli_game.py` is a basic terminal version of the Guess the Number game. It is useful for teaching how a normal Python program differs from a web app.

## Run it

In a terminal, open this project folder and run:

```bash
python3 cli_game.py
```

No extra libraries need to be installed. The `random` library is included with Python.

## Example game

```text
🎯 Welcome to Guess the Number!
I have chosen a number between 1 and 100.
Enter your guess: 50
Too high! Try a smaller number.
Enter your guess: 25
Too low! Try a bigger number.
Enter your guess: 37
You got it in 3 attempts! 🎉
Would you like to play again? (yes/no): no
Thanks for playing. Goodbye!
```

## How the code works

### `print()` shows text

```python
print("Too low! Try a bigger number.")
```

This writes a message to the terminal.

### `input()` gets text from the player

```python
guess = int(input("Enter your guess: "))
```

`input()` waits for the player to type something and press Enter. It returns text, so `int()` converts that text into a whole number.

### `try` and `except` handle mistakes

If a player types `hello` instead of a number, `int("hello")` would cause an error. The `try` / `except` section catches that error and politely asks for a whole number instead.

### `while True` repeats the game

```python
while True:
    # ask for a guess and check it
```

This loop repeats forever until the code reaches `break`. The `break` runs after the player guesses the correct number.

## CLI program vs Streamlit web app

| Command-line program (`cli_game.py`) | Streamlit web app (`app.py`) |
| --- | --- |
| Runs inside a terminal. | Runs in a web browser. |
| Uses `print()` to show messages. | Uses `st.write()`, `st.info()`, and `st.success()`. |
| Uses `input()` to receive the player's answer. | Uses a number box and buttons. |
| Starts at the first line and waits for input. | Streamlit reruns the file after interactions. |
| Uses ordinary variables while the game runs. | Uses `st.session_state` to remember values between reruns. |
| Does not need installation beyond Python. | Needs the Streamlit library. |

## A simple teaching order

1. Run `cli_game.py` first and explain `print`, `input`, variables, loops, and `if` statements.
2. Ask students to change the number range from 1–100 to 1–20.
3. Run `app.py` with Streamlit.
4. Compare how the same game uses visual controls instead of terminal text.
5. Explain why the web version needs `st.session_state` but the CLI version does not.
