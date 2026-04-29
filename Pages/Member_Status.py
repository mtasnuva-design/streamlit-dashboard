import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1= pd.read_excel("F:\\Drive D\\AI Training\\python_venv\\Session\\Dataset\\Q1Issue.xlsx")
st.subheader("Members wise Total Defcet count for Q1",)
total_member_defect =df1.groupby("Members")[["Critical","Major","Minor","Total Defect"]].sum().reset_index()
total_member_defect = total_member_defect.sort_values(by="Total Defect", ascending=True)

chart_member_defect = total_member_defect.melt(
    id_vars="Members",
    value_vars= ["Critical","Major","Minor"],
    var_name= "Defect Type",
    value_name= "Count"
)

fig_total_member_defect= px.bar(
    chart_member_defect,
    x="Count",
    y="Members",
    color="Defect Type",
    barmode="group",
    orientation="h",
    hover_data=["Count"]
)
    
st.plotly_chart(fig_total_member_defect,use_container_width=True)