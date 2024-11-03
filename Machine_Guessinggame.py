import streamlit as st
import random
def machine_guessinggame():
    if 'secret' not in st.session_state:
        st.session_state['secret'] = None
    if 'attempt' not in st.session_state:
        st.session_state['attempt'] = 0
    if 'guess' not in st.session_state:
        st.session_state['guess'] = random.randint(1,10)
    if 'result' not in st.session_state:
        st.session_state['result'] = ""
        
    
    st.title("GUESSING GAME")
    st.write("How to play?")
    st.write("1.Enter a number between 1 to 10 in the input box")
    st.write("2.Click Start_guessing button and let the machine guess your number")
    st.write("3.If machine guesses your number then it will return an response")
    st.write("4.If machine guesses an incorrect answer then start clicking Start_guessing button for 10 attempts")
    
    secret_input = st.text_input("Enter a number between 1 and 10 for the machine to guess:")

    if secret_input.isdigit() and 1 <= int(secret_input) <= 10:
        st.session_state['secret'] = int(secret_input)    
    
    def guessing():
         if st.session_state['attempt'] < 10:
            st.session_state['attempt'] += 1
            st.session_state['guess'] = random.randint(1, 10)

            if st.session_state['guess'] == st.session_state['secret']:
                st.session_state['result'] = f"The machine guessed the correct answer {st.session_state['secret']} in {st.session_state['attempt']} attempts!"
                return
            else:
                st.session_state['result'] = f"Attempt {st.session_state['attempt']}: The machine guessed {st.session_state['guess']}"

            if st.session_state['attempt'] >= 10 and st.session_state['guess'] != st.session_state['secret']:
                st.session_state['result'] = "The machine couldn't guess within 10 attempts."
                
                
    st.button(label="Start_Guessing",on_click=guessing)  
    st.write(st.session_state['result'])
    
    def playagain():
        st.session_state['attempt'] = 0
        st.session_state['guess'] = random.randint(1, 10)
        st.session_state['result'] = ""
        st.session_state['secret'] = ""
    
    st.button(label="Play Again",on_click=playagain)
  