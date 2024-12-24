import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import numpy as np

# Load pre-trained models (replace with your actual model path)
engagement_model = joblib.load('engagement_model.pkl')  # Engagement model
experience_model = joblib.load('experience_model.pkl')  # Experience model
satisfaction_model = joblib.load('satisfaction_model.pkl')  # Satisfaction model

# Sidebar with navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Dashboard",
        options=["User Overview", "Engagement Analysis", "Experience Analysis", "Satisfaction Analysis"],
        icons=["house", "graph-up", "speedometer", "smile"],
        default_index=0,
    )

# **User Overview Section**
if selected == "User Overview":
    st.title("User Overview Analysis")
    # Call your user overview functions here (e.g., user overview plot)
    st.write("Display your user overview insights here.")

# **Engagement Analysis Section**
elif selected == "Engagement Analysis":
    st.title("User Engagement Analysis")
    
    # User inputs for testing engagement model
    with st.form(key='engagement_form'):
        session_duration = st.number_input("Session Duration (s)", min_value=0)
        total_traffic = st.number_input("Total Traffic (Bytes)", min_value=0)
        submit_button = st.form_submit_button(label="Predict Engagement Score")

    if submit_button:
        input_features = np.array([[session_duration, total_traffic]])
        engagement_score = engagement_model.predict(input_features)
        st.write(f"Predicted Engagement Score: {engagement_score[0]:.2f}")

    # Example plot for Engagement (adjust as needed)
    st.bar_chart([session_duration, total_traffic], x=["Session Duration", "Total Traffic"], y=["Score"])

# **Experience Analysis Section**
elif selected == "Experience Analysis":
    st.title("Experience Analysis")
    
    # User inputs for testing experience model
    with st.form(key='experience_form'):
        tcp_retrans = st.number_input("Avg TCP Retransmission", min_value=0)
        avg_rtt = st.number_input("Avg RTT (ms)", min_value=0)
        avg_throughput = st.number_input("Avg Throughput (kbps)", min_value=0)
        submit_button = st.form_submit_button(label="Predict Experience Score")

    if submit_button:
        input_features = np.array([[tcp_retrans, avg_rtt, avg_throughput]])
        experience_score = experience_model.predict(input_features)
        st.write(f"Predicted Experience Score: {experience_score[0]:.2f}")

    # Example plot for Experience (adjust as needed)
    st.line_chart([tcp_retrans, avg_rtt, avg_throughput], x=["TCP Retrans", "RTT", "Throughput"], y=["Score"])

# **Satisfaction Analysis Section**
elif selected == "Satisfaction Analysis":
    st.title("Satisfaction Analysis")
    
    # User inputs for testing satisfaction model
    with st.form(key='satisfaction_form'):
        session_duration = st.number_input("Session Duration (s)", min_value=0)
        total_traffic = st.number_input("Total Traffic (Bytes)", min_value=0)
        tcp_retrans = st.number_input("Avg TCP Retransmission", min_value=0)
        avg_rtt = st.number_input("Avg RTT (ms)", min_value=0)
        avg_throughput = st.number_input("Avg Throughput (kbps)", min_value=0)
        submit_button = st.form_submit_button(label="Predict Satisfaction Score")

    if submit_button:
        input_features = np.array([[session_duration, total_traffic, tcp_retrans, avg_rtt, avg_throughput]])
        satisfaction_score = satisfaction_model.predict(input_features)
        st.write(f"Predicted Satisfaction Score: {satisfaction_score[0]:.2f}")

    # Example plot for Satisfaction (adjust as needed)
    st.area_chart([session_duration, total_traffic, tcp_retrans, avg_rtt, avg_throughput])

