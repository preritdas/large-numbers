import streamlit as st
import random

st.title("Law of Large Numbers")

# How many random trials
iterations = st.slider(label = "Number of iterations.", min_value = 5, max_value = 10000, value = 50)

x = [_ for _ in range(iterations)] # create an array of consecutive integers
y = [random.randint(0, 1) for _ in range(iterations)] # pick a random number for every iteration

st.subheader("Your Random Numbers")

st.line_chart(y)

st.subheader("Moving Average")

# Calculate average
avg = []
total = 0
for pos, item in enumerate(y):
    total += item # maintain a running total
    avg.append(total/(pos+1)) # append avg with moving average

st.line_chart(avg)