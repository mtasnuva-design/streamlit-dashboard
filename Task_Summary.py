import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Dashboard",
    page_icon=":bar_chart:",
)

project_1_page = st.Page(
    page="Task_Summary.py",
    title="Task Summary",
    default=True,
)

project_2_page = st.Page(
    page="Pages/Project_Status.py",
    title="Project Status",

)

project_3_page = st.Page(
    page="Pages/Member_Status.py",
    title="Member Status",

)
st.title("Task summary for Q1")
st.divider()
st.sidebar.success("Select a page above")
st.logo("Logo/samsung-logo.jpg")

col1, col2= st.columns(2,gap="medium")
with col1:
    st.subheader("Galaxy Live Ops")
    st.write("""
        * Promotional App Verified: 8
        * Issue Reported: 14
        * Total TC Executed: 738
        """
        )
    st.write("\n")
    st.subheader("GStore:Merchandising")
    st.write("""
        * Galaxy App Verified: 21
        * Issue Reported: 345 (A:4)
        * Total TC Executed: 1133
        """
        )
  
    st.write("\n")
    st.subheader("Weekly Calendar-US")
    st.write("""
        * Total Contents Verified: 189
        * Issue Reported: 2
        * Total TC Executed: 224670
        """
        )
    st.write("\n")
    st.subheader("Weekly Calendar-Canada")
    st.write("""
        * Total Contents Verified: 189
        * Issue Reported: 2
        * Total TC Executed: 220375
        """
        )
    
    with col2:
        st.subheader("GS Benefits")
        st.write("""
           * App Verified Request: 16
           * Issue Reported: 14
           * Total TC Executed: 1117
           """
           )
        st.write("\n")
        st.subheader("The SIX-TV App")
        st.write("""
           * App Verified : 1
           * Issue Verified: 1
           * Total TC Executed: 32
           """
           )
        
        st.write("\n")
        st.subheader("GameBreak test on TV Plus")
        st.write("""
           * Total Channels Verified : 82
           * Issue Reported: 22
           * Issue Verified: 16
           * Total TC Executed: 1936
           * Total TC Developed: 160
           """
           )
        
        st.write("\n")
        st.subheader("Duck Hunt-TV App")
        st.write("""
           * App Verified : 6
           * Issue Reported: 5
           * Issue Verified : 20  
           * Total TC Executed: 294
           * Total TC Developed: 114
           """
           )