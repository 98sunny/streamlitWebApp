import streamlit as st
import matplotlib.pyplot as plt
imprt seaborn as sns
import numpy as np
import base64
import pandas as pd
import seaborn as sns

st.title('NBA Player Stats Explorer')

st.markdown("""
This app does web scraping of player stats of NBA
Python Libraries used: base6,streamlit, pandas.
Date Scores: https://www.basketball-reference.com/

"""
)

st.sidebar.heade('User Input Feaures')
selected_year=st.sidebar('Year',list(reversed(range(1950,2021))))
