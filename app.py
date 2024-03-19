import streamlit as st
from game_logic import play_game, save_player_data

def main():
    st.title("Guess the Number Game")

    name = st.text_input("Enter Full Name:")
    if name:
        name = name.upper()
        st.write(f"Hi, {name}!")

        play = st.button("Play Game")
        if play:
            score, streak = play_game(name)
            st.write("SCORE:", score)
            save_player_data(name, score, streak)
            st.write("Game Over!")

if __name__ == "__main__":
    main()
