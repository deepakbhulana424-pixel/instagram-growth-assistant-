

import random
import streamlit as st

st.set_page_config(
    page_title="Instagram Growth Assistant",
    page_icon="📈"
)

st.title("📈 Instagram Growth Assistant")
st.write("Apni Hindi Reels ke liye ideas, hooks aur scripts banao!")

ideas = {
    "AI Video": [
        {
            "title": "Sapno ki duniya",
            "hook": "Socho, agar tumhara sapna saamne aa jaye!",
            "dialogue": "Kaash har sapna sirf dekha nahi, jiya bhi ja sakta!",
            "scenes": ["Normal room", "AI fantasy world", "Surprised reaction"]
        },
        {
            "title": "Cinematic photo",
            "hook": "Ek normal photo ko movie jaisa bana sakte ho!",
            "dialogue": "Photo wahi, lekin andaaz bilkul filmy!",
            "scenes": ["Normal portrait", "Cinematic lighting", "Final reveal"]
        },
        {
            "title": "Future ka gaon",
            "hook": "Agar hamara gaon 100 saal baad aisa dikhe?",
            "dialogue": "Parampara bhi apni, technology bhi apni!",
            "scenes": ["Aaj ka gaon", "Future buildings", "Aerial view"]
        }
    ],
    "Desi Comedy": [
        {
            "title": "Papa ne phone maanga",
            "hook": "Jab papa bolein, zara phone dena!",
            "dialogue": "Papa: Phone do!\nBeta: Papa, pehle batao kya dekhna hai!",
            "scenes": ["Beta phone chhupata hai", "Papa phone maangte hain", "Funny reaction"]
        },
        {
            "title": "Udhar wala dost",
            "hook": "Har group mein ek aisa dost hota hai!",
            "dialogue": "Dost: Tu mera bhai hai!\nMain: Toh bhai, paise wapas kar!",
            "scenes": ["Paise maangna", "Paise milna", "Phone silent"]
        },
        {
            "title": "Mummy ka Wi-Fi",
            "hook": "Jab mummy Wi-Fi band karne ki dhamki dein!",
            "dialogue": "Mummy: Phone band kar!\nBeta: Online class hai!\nMummy: Teacher ka naam bata!",
            "scenes": ["Reel dekhna", "Mummy aati hain", "Beta padhai ki acting karta hai"]
        }
    ],
    "Motivational Shayari": [
        {
            "title": "Maa ke sapne",
            "hook": "Maa ke chehre par khushi laani hai!",
            "dialogue": "Thak jaaun toh maa ka chehra yaad aata hai,\nMera har sapna mujhe unke liye jagata hai.",
            "scenes": ["Subah ki mehnat", "Mushkilon ka saamna", "Maa ki muskaan"]
        },
        {
            "title": "Haar ke baad jeet",
            "hook": "Haar gaye ho? Kahani abhi khatam nahi hui!",
            "dialogue": "Girkar sambhalna seekh liya hai,\nAb waqt ko badalna seekh liya hai.",
            "scenes": ["Niraasha", "Dobara koshish", "Progress"]
        },
        {
            "title": "Papa ki mehnat",
            "hook": "Papa ki khamoshi ke peeche kitne sapne hote hain!",
            "dialogue": "Papa khud dhoop mein jalte rahe,\nTaaki hum aage badhte rahein.",
            "scenes": ["Papa kaam karte hue", "Beta samajhta hai", "Beta mehnat karta hai"]
        }
    ],
    "Attitude": [
        {
            "title": "Apni pehchaan",
            "hook": "Naam chahiye toh kaam aisa karo!",
            "dialogue": "Bheed ka hissa nahi banna,\nApni pehchaan khud banana hai.",
            "scenes": ["Confident walk", "Mehnat", "Final pose"]
        },
        {
            "title": "Khamoshi se mehnat",
            "hook": "Har baat ka jawab dena zaroori nahi!",
            "dialogue": "Abhi khamosh hoon, kamzor nahi,\nMera waqt aayega, bas shor nahi.",
            "scenes": ["Log mazaak banate hain", "Mehnat", "Result"]
        }
    ],
    "Emotional Story": [
        {
            "title": "Papa ka purana joota",
            "hook": "Us din bete ko papa ki mehnat samajh aayi!",
            "dialogue": "Beta: Papa, naya joota kyun nahi lete?\nPapa: Pehle tere sapne poore kar loon, beta.",
            "scenes": ["Purana joota", "Papa ki mehnat", "Gale lagna"]
        },
        {
            "title": "Maa ka intezaar",
            "hook": "Maa aaj bhi darwaze par tumhara intezaar karti hai!",
            "dialogue": "Duniya kitni bhi badi ho jaaye,\nMaa ke liye bachcha hamesha bachcha rehta hai.",
            "scenes": ["Maa intezaar karti hai", "Beta ghar lautata hai", "Maa gale lagati hai"]
        }
    ]
}

topic = st.selectbox("🎬 Reel ka topic chuno", list(ideas.keys()))
duration = st.selectbox("⏱️ Reel duration", ["10 seconds", "15 seconds", "30 seconds"])
count = st.slider("💡 Kitne ideas chahiye?", 1, 5, 3)

if st.button("🚀 Mere Reel Ideas Banao", use_container_width=True):
    st.session_state["generated"] = random.sample(
        ideas[topic], min(count, len(ideas[topic]))
    )

if "generated" in st.session_state:
    for i, idea in enumerate(st.session_state["generated"], start=1):
        st.divider()
        st.subheader(f"🎥 Idea {i}: {idea['title']}")
        st.markdown("**🎯 Hook**")
        st.write(idea["hook"])
        st.markdown("**🎬 Scene-by-scene plan**")
        for scene in idea["scenes"]:
            st.write(f"• {scene}")
        st.markdown("**🗣️ Hindi dialogue / voiceover**")
        st.write(idea["dialogue"])
        st.markdown("**✍️ Caption**")
        st.write(f"{idea['title']} ❤️ Aapki kya rai hai? Comment mein batao!")
        st.markdown("**#️⃣ Hashtags**")
        st.write("#HindiReels #InstagramIndia #ReelsIdeas #DigitalCreator #HindiContent")
        st.markdown("**🏁 Ending**")
        st.write("Aisi aur videos ke liye follow karein aur apni rai comment karein.")
        st.caption(f"Suggested duration: {duration}")

    if st.button("🔄 Aur naye ideas banao"):
        st.rerun()

st.divider()
st.caption("Original content banao; growth ki guarantee nahi hoti.")
