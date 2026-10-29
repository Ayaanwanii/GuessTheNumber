"""A beginner-friendly Guess the Number game made with Streamlit."""

import random

import streamlit as st


# Set the browser tab title and the layout of the page.
st.set_page_config(page_title="Guess the Number", page_icon="🎯")


def start_new_game():
    """Put fresh game values into Streamlit's memory."""
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_won = False
    st.session_state.message = "I picked a number from 1 to 100. Can you find it?"


# Streamlit reruns this file after each click. session_state lets us remember
# the number and attempt count between those reruns.
if "secret_number" not in st.session_state:
    start_new_game()


st.title("🎯 Guess the Number")
st.write("Try to guess the secret number between **1 and 100**.")

with st.sidebar:
    st.header("Game controls")
    if st.button("Start a new game"):
        start_new_game()
        st.rerun()


# A number_input only allows numbers in the range we choose.
guess = st.number_input(
    "Your guess",
    min_value=1,
    max_value=100,
    value=50,
    step=1,
    disabled=st.session_state.game_won,
)

if st.button("Check my guess", disabled=st.session_state.game_won):
    st.session_state.attempts += 1

    # Compare the player's guess to the computer's secret number.
    if guess < st.session_state.secret_number:
        st.session_state.message = "Too low! Try a bigger number."
    elif guess > st.session_state.secret_number:
        st.session_state.message = "Too high! Try a smaller number."
    else:
        st.session_state.message = "You got it! Great guessing! 🎉"
        st.session_state.game_won = True


if st.session_state.game_won:
    st.success(st.session_state.message)
else:
    st.info(st.session_state.message)

st.write(f"**Attempts:** {st.session_state.attempts}")

if st.session_state.game_won:
    st.balloons()
    st.write("Press **Start a new game** in the sidebar to play again.")
