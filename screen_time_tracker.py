import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📱 Screen Time Tracker", layout="centered")
st.title("📱 Screen Time Tracker")
st.subheader("Track your daily screen time & stay balanced! 🌿")

# Input Fields
social = st.number_input("🕒 Social Media (minutes)", min_value=0)
videos = st.number_input("🎬 Watching Videos (minutes)", min_value=0)
study = st.number_input("📚 Online Classes/Study (minutes)", min_value=0)
games = st.number_input("🎮 Gaming (minutes)", min_value=0)
other = st.number_input("🔧 Other Apps (minutes)", min_value=0)

if st.button("Track My Screen Time"):
    # Total time
    total = social + videos + study + games + other
    
    if total == 0:
        st.warning("Please enter your screen time above.")
    else:
        # Pie chart
        labels = ['Social Media', 'Videos', 'Study', 'Gaming', 'Other']
        values = [social, videos, study, games, other]
        
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        # Productivity Score
        productive = study
        unproductive = total - study
        score = round((productive / total) * 100, 2)

        st.markdown(f"### ✅ Productivity Score: **{score}%**")
        
        if score >= 70:
            st.success("Great job! You're managing screen time well. ✅")
        elif score >= 40:
            st.info("Doing okay, but try to reduce distractions. 🌿")
        else:
            st.warning("Too much time on distractions! Try to focus more. 🚫")

        # Tips
        st.markdown("---")
        st.subheader("💡 Tips to Reduce Screen Time")
        st.markdown("""
        - ⏰ Set app time limits  
        - 🚶 Take screen breaks every 30 mins  
        - 🎯 Use focus mode while studying  
        - 📵 Avoid screen 1 hour before sleep  
        """)
