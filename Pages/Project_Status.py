import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from PIL import Image
import os
import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel("F:\\Drive D\\AI Training\\python_venv\\Session\\Dataset\\Qtr.xlsx")

st.set_page_config(page_title="Quaterly Report!!!", page_icon=":bar_chart:",layout="wide")


st.subheader("Project Status for Q1")
    
st.divider()      

col1, col2 = st.columns([0.5,0.5])


total_task = int(df["Total Task Request"].sum())
total_app = int(df["Total app Verified"].sum())
total_content = int(df["Total Content Verified"].sum())
total_issue = int(df["Total Issue"].sum())

with col1:
    st.write(f"Total Task Request: {total_task}")
    st.write(f"Total app Verified: {total_app}")

with col2:
    st.write(f"Total Content Verified: {total_content}")
    st.write(f"Total Issue Posted: {total_issue}")



col3, col4 = st.columns([0.5,0.5])

# Application wise total Task Request [bar chart]
with col3:

    total_task_request = (df.groupby(by=["Application"]).sum()[["Total Task Request"]].sort_values(by="Total Task Request"))

    fig_total_task_request = px.bar(
        total_task_request,
        x="Total Task Request",
        y=total_task_request.index,
        orientation="h",
        title="<b>Application wise total Task Request</b>",
        color_discrete_sequence=["#0083B8"]*len(total_task_request),
        template="plotly_white",

        )

    fig_total_task_request.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
    st.plotly_chart(fig_total_task_request)

# Application wise total TC Execution [bar chart]
with col4:
    
    total_tc_executed = (df.groupby(by=["Application"]).sum()[["Total TC Executed"]].sort_values(by="Total TC Executed"))

    fig_total_tc_executed = px.bar(
        total_tc_executed,
        x="Total TC Executed",
        y=total_tc_executed.index,
        orientation="h",
        title="<b>Application wise total TC Execution</b>",
        color_discrete_sequence=["#0083B8"]*len(total_tc_executed),
        template="plotly_white",

        )

    fig_total_tc_executed.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
    st.plotly_chart(fig_total_tc_executed)

st.divider()    

col5, col6 = st.columns([0.5,0.5])

# Total App Verified [bar chart]
with col5:

    total_app_verified = (df.groupby(by=["Application"]).sum()[["Total app Verified"]])

    fig_total_app_verified = px.bar(
        total_app_verified,
        x=total_app_verified.index,
        y="Total app Verified",
        orientation="v",
        title="<b>Total App Verified</b>",
        color_discrete_sequence=["#0083B8"]*len(total_app_verified),
        template="plotly_white",

        )

    fig_total_app_verified.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
    st.plotly_chart(fig_total_app_verified)

# Total Content Verified [bar chart]
with col6:
    
    total_content_verified = (df.groupby(by=["Application"]).sum()[["Total Content Verified"]])

    fig_total_content_verified = px.bar(
        total_content_verified,
        x=total_content_verified.index,
        y="Total Content Verified",
        orientation="v",
        title="<b>Total Content Verified</b>",
        color_discrete_sequence=["#0083B8"]*len(total_tc_executed),
        template="plotly_white",

        )

    fig_total_content_verified.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
        )
    st.plotly_chart(fig_total_content_verified)

st.divider()
# Priority wise Total Defect [bar chart]

    
total_defect = df.groupby("Application")[["Critical","Major","Minor"]].sum().reset_index()

chart_total_defect = total_defect.melt(
    id_vars="Application",
    value_vars= ["Critical","Major","Minor"],
    var_name= "Defect Type",
    value_name= "Count"
    )

fig_total_defect= px.bar(
    chart_total_defect,
    x="Application",
    y="Count",
    color="Defect Type",
    barmode="group",
    title="Priority wise Total Defect",
    hover_data=["Count"]
    )
    
st.plotly_chart(fig_total_defect,use_container_width=True)
st.divider()
# Total Testcases Developed [Pie chart]    

total_tc_develop = df.groupby("Application").sum()["Total TC Developed"].reset_index()
   
fig_total_tc_develop=px.pie(total_tc_develop, values="Total TC Developed", names="Application", title="Total TC Development Status")
st.plotly_chart(fig_total_tc_develop)

st.divider()