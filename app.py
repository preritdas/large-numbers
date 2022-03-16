import streamlit as st
import random

st.set_page_config(page_title = "Law of Large Numbers", page_icon = ":chart_with_upwards_trend:")
st.title("The Law of Large Numbers")

# Style
def use_style(file_path: str):
    with open(file_path, 'r') as f:
        content = f.read()
        st.markdown(f"<style>{content}</style>", unsafe_allow_html=True)
use_style('style/style.css')

# How many random trials
iterations = st.slider(label = "Choose the number of iterations.", min_value = 5, max_value = 10000, value = 50)

x = [_ for _ in range(iterations)] # create an array of consecutive integers
y = [random.randint(0, 1) for _ in range(iterations)] # pick a random number for every iteration

st.subheader("Average Value")

# Calculate average
avg = []
total = 0
for pos, item in enumerate(y):
    total += item # maintain a running total
    avg.append(total/(pos+1)) # append avg with moving average

st.line_chart(avg)

if iterations < 500:
    st.subheader("Your Random Numbers")
    st.line_chart(y)

st.write(
    """
    ----
    Press `'r'` to repeat the simulation with the same input variables.
    """
)