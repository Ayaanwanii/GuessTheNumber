"""Vercel-compatible web version of the Guess the Number game.

Vercel looks for a top-level variable named ``app`` in Python web functions.
This file provides that Flask application. The original Streamlit game remains
in app.py and can still be run locally with: streamlit run app.py
"""

import os
import random

from flask import Flask, redirect, render_template_string, request, session, url_for


app = Flask(__name__)

# Vercel deployments should set SECRET_KEY in Project Settings > Environment Variables.
# The fallback lets the project work locally for a short demo.
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key-before-production")


PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Guess the Number</title>
  <style>
    body { background: #f0f4ff; color: #18213c; font-family: Arial, sans-serif; margin: 0; }
    main { background: white; border-radius: 16px; box-shadow: 0 8px 25px #b9c5e6; margin: 70px auto; max-width: 480px; padding: 32px; text-align: center; }
    input, button { border-radius: 8px; font-size: 1rem; padding: 12px; }
    input { border: 1px solid #a9b7dc; width: 120px; }
    button { background: #4169e1; border: 0; color: white; cursor: pointer; font-weight: bold; }
    .message { background: #e8efff; border-radius: 8px; margin: 20px 0; padding: 14px; }
    .success { background: #d9f7df; color: #155d25; }
    a { color: #4169e1; }
  </style>
</head>
<body>
  <main>
    <h1>🎯 Guess the Number</h1>
    <p>I picked a number from <strong>1 to 100</strong>. Can you find it?</p>
    {% if message %}
      <p class="message {% if won %}success{% endif %}">{{ message }}</p>
    {% endif %}
    {% if not won %}
      <form method="post">
        <label for="guess">Your guess</label><br><br>
        <input id="guess" name="guess" type="number" min="1" max="100" required autofocus>
        <button type="submit">Check my guess</button>
      </form>
    {% endif %}
    <p><strong>Attempts:</strong> {{ attempts }}</p>
    {% if won %}<p>🎉 Excellent work!</p>{% endif %}
    <p><a href="{{ url_for('new_game') }}">Start a new game</a></p>
  </main>
</body>
</html>
"""


def start_new_game():
    """Store fresh game values in this player's browser session."""
    session["secret_number"] = random.randint(1, 100)
    session["attempts"] = 0
    session["won"] = False
    session["message"] = ""


@app.route("/", methods=["GET", "POST"])
def home():
    """Display the game and process a player's guess."""
    if "secret_number" not in session:
        start_new_game()

    if request.method == "POST" and not session["won"]:
        guess = int(request.form["guess"])
        session["attempts"] += 1

        if guess < session["secret_number"]:
            session["message"] = "Too low! Try a bigger number."
        elif guess > session["secret_number"]:
            session["message"] = "Too high! Try a smaller number."
        else:
            session["message"] = "You got it! Great guessing!"
            session["won"] = True

    return render_template_string(
        PAGE,
        attempts=session["attempts"],
        message=session["message"],
        won=session["won"],
    )


@app.route("/new-game")
def new_game():
    """Reset the game, then return the player to the home page."""
    start_new_game()
    return redirect(url_for("home"))
