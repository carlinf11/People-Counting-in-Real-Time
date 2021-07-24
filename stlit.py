import streamlit as st
import pandas as pd
import numpy as np
import time, schedule, csv

import importlib


st.title("PORJECT 001")

if st.button("RUN THE MODEL"):
    import Run 
    data=pd.read_csv("Log.csv")
    st.dataframe(data)
    st.success("MODEL SUCCESSFULLY EXECUTED ")
