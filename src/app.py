import streamlit as st
from src.run import monty_hall , simulate_monty_hall
import time


st.title('Monty Hall Simulation')
st.image('data:image/jpeg;base64,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')

user_input = st.selectbox('What do you want ?', (None, 'what  Monty Hall problem is ?', 'Simulate The Monty hall problem'))

if user_input == None:
    pass
elif user_input == 'what  Monty Hall problem is ?':
    st.title("The Monty Hall Problem")

    st.write("The Monty Hall problem is a famous probability puzzle named after the host of the game show 'Let's Make a Deal,' Monty Hall. Here's a step-by-step explanation:")

    st.subheader("Scenario")
    st.write("Imagine you're a contestant on a game show. There are three doors: behind one door is a valuable prize (let's say a car), and behind the other two doors are less desirable prizes (let's say goats).")

    st.subheader("Steps")
    st.write("**Initial Choice:**")
    st.write("- You pick one door, hoping to find the car behind it.")

    st.write("**Reveal:**")
    st.write("- Before opening the chosen door, the host (Monty) opens one of the remaining two doors that doesn't have the car behind it, revealing a goat.")
    st.write("- At this point, there are two unopened doors: one you initially chose and one other unopened door.")

    st.write("**Decision Point:**")
    st.write("- Now, the host gives you a choice: stick with your initial choice or switch to the other unopened door.")

    st.subheader("The Dilemma")
    st.write("The key question here is: Is it advantageous to switch your choice?")

    st.subheader("Explanation")
    st.write("- Initially, it might seem that both unopened doors have an equal chance (50%) of hiding the car.")
    st.write("- However, statistically, it's more beneficial to switch your choice after the host reveals a goat behind one of the doors.")

    st.subheader("Probability Explanation")
    st.write("- When you initially pick a door, there's a 1/3 chance of selecting the car and a 2/3 chance of picking a goat.")
    st.write("- When the host reveals a goat behind one of the other doors, the initial probabilities don't change for your chosen door (1/3 for the car, 2/3 for a goat).")
    st.write("- The crucial insight is that if you switch, you now have a 2/3 chance of winning the car because the 2/3 probability that you initially picked a goat is now concentrated in the other unopened door.")

    st.subheader("Conclusion")
    st.write("The optimal strategy is to always switch your choice after the host reveals a goat. Counterintuitively, this strategy increases your chances of winning the car from 1/3 to 2/3.")

    st.subheader("Reference")
    st.write("- The problem gained prominence after it was popularized by Marilyn vos Savant in her column 'Ask Marilyn' in *Parade* magazine in 1990.")
    st.write("- The Monty Hall problem can be explored mathematically using conditional probability and Bayes' theorem.")
    st.write("- This problem challenges our intuition about probability and has sparked debates and discussions about its solution among mathematicians and enthusiasts alike.")
else :
    user_mode = st.radio('Choice Your Mode',('Switch My Choice', 'Stay on my Choice'))
    if user_mode == 'Switch My Choice' :
        mode = 'switch'
    else :
        mode = 'stay'
    user_times = st.number_input('How many times do you want to simulate?',min_value=1,max_value=100000,value=100)
    clicked = st.button('Click here to simulate')
    chart1 = st.line_chart(x = None, y = None)
    win_counter=0
    if clicked :
        for i in range(user_times) :
            win_counter += simulate_monty_hall(times=1, mode= mode)[1]
            chart1.add_rows([win_counter/ (i + 1)])
            time.sleep(0.01)



