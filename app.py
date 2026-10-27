import streamlit as st
import random

st.set_page_config(page_title="Instagram Growth Assistant", page_icon="📈")
st.title("📈 Instagram Growth Assistant")
st.write("Apni Hindi Reels ke liye ideas, hooks aur captions banao.")

topic = st.selectbox("Reel ka topic chuno", ["AI Video", "Desi Comedy", "Motivational Shayari", "Attitude", "Emotional Story"])

if st.button("Mere Reel Ideas Banao"):
    ideas = {
        "AI Video": ["Agar AI se sapno ki duniya bana sakte?", "Normal photo ko cinematic kaise dikhayein?"],
        "Desi Comedy": ["Jab papa achanak phone check karein!", "Dost udhaar lekar gayab ho jaye!"],
        "Motivational Shayari": ["Maa ke sapne poore karne ka junoon", "Haar ke baad dobara khade hone ki kahani"],
        "Attitude": ["Apni pehchaan khud banao", "Khamoshi se mehnat, result se jawab"],
        "Emotional Story": ["Papa ki mehnat ko samajhne wali kahani", "Ek chhoti madad jo zindagi badal de"]
    }
    idea = random.choice(ideas[topic])
    st.subheader("🎬 Reel Idea")
    st.write(idea)
    st.subheader("🎯 Hook")
    st.write(idea + " — end tak zaroor dekhna!")
    st.subheader("✍️ Caption")
    st.write("Aapki kya rai hai? Comment mein zaroor batao ❤️")
    st.subheader("#️⃣ Hashtags")
    st.write("#HindiReels #InstagramIndia #ReelsIdeas #DigitalCreator")

st.caption("Original content banao; growth ki guarantee nahi hoti.")
