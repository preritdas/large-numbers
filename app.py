# Non-local imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Local imports
import random


# Page configuration
st.set_page_config(page_title = "Law of Large Numbers", page_icon = ":chart_with_upwards_trend:", layout = "wide")
st.title("The Law of Large Numbers")

# Style
def use_style(file_path: str):
    with open(file_path, 'r') as f:
        content = f.read()
        st.markdown(f"<style>{content}</style>", unsafe_allow_html=True)
use_style('style/style.css')

# Distribution  with a menu
distribution_type = option_menu(
    menu_title = "Distribution Type",
    options = ["Perfectly Random", "Normal"],
    menu_icon = "bar-chart-fill",
    icons = ["asterisk", "bar-chart"]
)

# How many random trials
iterations = st.slider(label = "Choose the number of iterations.", min_value = 5, max_value = 10000, value = 50)
# Min and Max
slider_label = "Choose your values. If you leave this slider untouched, the program will simulate coin flips."
min_value, max_value = st.slider(label = slider_label, max_value = 1000, value = (0, 1))
inputs_mean = np.mean([min_value, max_value])



# Determine the data
x = [_ for _ in range(iterations)] # create an array of consecutive integers
if distribution_type == 'Perfectly Random':
    y = [random.randint(min_value, max_value) for _ in range(iterations)] # pick a random number for every iteration
elif distribution_type == 'Normal':
    y = list(np.random.normal(loc = inputs_mean, scale = inputs_mean, size = iterations))
    for i in range(len(y)):
        y[i] = round(y[i])

if distribution_type == 'Perfectly Random':
    st.subheader("Average Value")

    # Calculate average
    avg = []
    list_of_5 = [np.mean([min_value, max_value]) for _ in range(iterations)]
    total = 0
    for pos, item in enumerate(y):
        total += item # maintain a running total
        avg.append(total/(pos+1)) # append avg with moving average

    plot_df = pd.DataFrame(
        {
            "Expected Value": list_of_5, 
            "Average Value": avg
        }
    )

    if st.checkbox("Show target expected value."):
        st.line_chart(plot_df)
    else:
        st.line_chart(plot_df['Average Value'])

    # Show Pyplot
    if st.checkbox("Show image-based pyplot chart."):
        fig, ax = plt.subplots()
        plt.style.use('fivethirtyeight')
        plt.title("Average Value")
        ax.plot(avg, label = "Current Average Value")
        ax.plot(list_of_5, label = "Expected Value")
        ax.legend()
        st.pyplot(fig)
elif distribution_type == 'Normal': 
    # st.subheader("Random Values")

    # Display Values
    values = y
    list_of_5 = [np.mean([min_value, max_value]) for _ in range(iterations)]

    plot_df = pd.DataFrame(
        {
            "Expected Value": list_of_5, 
            "Average Value": values
        }
    )

    # if st.checkbox("Show target expected value."):
    #     st.line_chart(plot_df)
    # else:
    #     st.line_chart(plot_df['Average Value'])

    # Show Pyplot
    if st.checkbox("Show image-based pyplot chart."):
        fig, ax = plt.subplots()
        plt.style.use('fivethirtyeight')
        plt.title("Average Value")
        ax.plot(values, label = "Current Average Value")
        ax.plot(list_of_5, label = "Expected Value")
        ax.legend()
        st.pyplot(fig)

# Show all values
if iterations < 500 or distribution_type == 'Normal':
    st.subheader("Your Random Numbers")
    st.line_chart(y)

# Show chart of all values
if True: #max_value != 1:
    st.subheader("Distribution of Random Selections")
    unique_numbers = list(np.unique(y))
    occurences = []
    for number in unique_numbers:
        occurences.append(list(y).count(number))
    chart_data = pd.DataFrame(
        {
            "Unique": unique_numbers,
            "Occurences": occurences
        }
    ).set_index('Unique')
    st.bar_chart(data = chart_data)

st.write(
    """
    ----
    Press `'r'` to repeat the simulation with the same input variables.
    """
) 
