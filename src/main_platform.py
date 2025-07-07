#!/usr/bin/env python3
"""
IBM Business Intelligence (BI) Analyst Platform
Main Application
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

def main():
    """Main application"""
    st.title("📊 IBM Business Intelligence (BI) Analyst")
    st.markdown("*Professional Capstone Project*")
    st.markdown("---")
    
    # Demo data
    data = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=30),
        'Value': np.random.randn(30).cumsum(),
        'Category': np.random.choice(['A', 'B', 'C'], 30)
    })
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Records", len(data))
    
    with col2:
        st.metric("Average Value", f"{data['Value'].mean():.2f}")
    
    with col3:
        st.metric("Categories", data['Category'].nunique())
    
    # Visualizations
    st.subheader("📈 Data Visualization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_line = px.line(data, x='Date', y='Value', title='Value Over Time')
        st.plotly_chart(fig_line, use_container_width=True)
    
    with col2:
        fig_bar = px.bar(data.groupby('Category')['Value'].sum().reset_index(), 
                        x='Category', y='Value', title='Value by Category')
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Data table
    st.subheader("📋 Data Table")
    st.dataframe(data, use_container_width=True)
    
    st.success("✅ IBM Business Intelligence (BI) Analyst Platform operational!")

if __name__ == "__main__":
    main()
