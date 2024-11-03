import streamlit as st
import random 
def user_guessinggame():
    if 'attempt' not in st.session_state:
        st.session_state['attempt'] = 0
        st.session_state['answer'] = random.randint(1,20)

    if 'result' not in st.session_state:
        st.session_state['result'] = ""

    st.title("GUESSING GAME")
    st.title("How to play?")
    st.write("1.Type an number in the range of 1 and 20 in the box")
    st.write("2.If your guess is correct then it will return congratulations")
    st.write("3.If your guess is incorrect then it will return try again")

    guess=st.number_input("Enter your guess",min_value=1,max_value=20)
        
    def guessing():
        st.session_state['attempt'] += 1
        if guess == st.session_state['answer']:
            st.session_state['result'] = f"Congratulations! You have guessed the number in {st.session_state['attempt']} attempts."
            st.session_state['attempt'] = 0
            st.session_state['answer'] = random.randint(1,20)
        elif st.session_state['answer'] in range(guess-5,guess+5):
            st.session_state['result']= "So Close!!! You are amazing, Please try in same way"
        else:
            st.session_state['result'] = "Sorry that's didn't get matched, Please try again"

    st.button(label="Submit",on_click=guessing)

    st.write(st.session_state['result'])

        