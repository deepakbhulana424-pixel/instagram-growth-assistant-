import random
import streamlit as st

st.set_page_config(page_title="Instagram Growth Assistant", page_icon="📈")

st.title("📈 Instagram Growth Assistant")
st.write("Apni Hindi Reels ke liye ideas, hooks aur scripts banao!")

IDEAS = {
    "AI Video": [
        ("Sapno ki duniya", "Socho, agar tumhara sapna saamne aa jaye!",
         "Kaash har sapna sirf dekha nahi, jiya bhi ja sakta hai!",
         ["Normal room", "AI fantasy world", "Surprised reaction"]),
        ("Cinematic photo", "Ek normal photo ko movie jaisa bana sakte ho!",
         "Photo wahi, lekin andaaz bilkul filmy!",
         ["Normal portrait", "Cinematic lighting", "Final reveal"]),
        ("Future ka gaon", "Agar hamara gaon 100 saal baad aisa dikhe?",
         "Parampara bhi apni, technology bhi apni!",
         ["Aaj ka gaon", "Future buildings", "Aerial view"]),
        ("Ek photo, teen duniya", "Ek photo se teen alag duniya dekhni hain?",
         "Soch ki koi limit nahi hoti!",
         ["Original photo", "Fantasy world", "Futuristic city"]),
        ("AI magic", "Ye magic nahi, AI ka kamaal hai!",
         "Technology se imagination ko nayi udaan do!",
         ["Normal scene", "Transformation", "Final result"]),
    ],
    "Desi Comedy": [
        ("Papa ne phone maanga", "Jab papa bolein, zara phone dena!",
         "Papa: Phone do!\\nBeta: Papa, pehle batao kya dekhna hai!",
         ["Beta phone chhupata hai", "Papa phone maangte hain", "Funny reaction"]),
        ("Udhar wala dost", "Har group mein ek aisa dost hota hai!",
         "Dost: Tu mera bhai hai!\\nMain: Toh bhai, paise wapas kar!",
         ["Paise maangna", "Paise milna", "Phone silent"]),
        ("Mummy ka Wi-Fi", "Jab mummy Wi-Fi band karne ki dhamki dein!",
         "Mummy: Phone band kar!\\nBeta: Online class hai!\\nMummy: Teacher ka naam bata!",
         ["Reel dekhna", "Mummy aati hain", "Beta padhai ki acting karta hai"]),
        ("Salary khatam", "Salary aane ke agle din ka haal!",
         "Dost: Salary aa gayi?\\nMain: Haan, par ab bank ko hi yaad hai!",
         ["Salary notification", "Bills aate hain", "Balance dekhkar shock"]),
        ("Late hone ka bahana", "Jab dost har baar late aaye!",
         "Dost: Bas 5 minute door hoon!\\nMain: Tu toh abhi ghar se nikla hi nahi!",
         ["Dost ka intezaar", "Phone call", "Funny reveal"]),
    ],
    "Motivational Shayari": [
        ("Maa ke sapne", "Maa ke chehre par khushi laani hai!",
         "Thak jaaun toh maa ka chehra yaad aata hai,\\nMera har sapna mujhe unke liye jagata hai.",
         ["Subah ki mehnat", "Mushkilon ka saamna", "Maa ki muskaan"]),
        ("Haar ke baad jeet", "Haar gaye ho? Kahani abhi khatam nahi hui!",
         "Girkar sambhalna seekh liya hai,\\nAb waqt ko badalna seekh liya hai.",
         ["Niraasha", "Dobara koshish", "Progress"]),
        ("Papa ki mehnat", "Papa ki khamoshi ke peeche kitne sapne hote hain!",
         "Papa khud dhoop mein jalte rahe,\\nTaaki hum aage badhte rahein.",
         ["Papa kaam karte hue", "Beta samajhta hai", "Beta mehnat karta hai"]),
        ("Khud ki pehchaan", "Doosron se nahi, kal wale khud se aage niklo!",
         "Raaste mushkil hain toh kya hua,\\nManzil apni hai, hausla bhi apna hoga.",
         ["Mehnat", "Koshish", "Confident finish"]),
        ("Kabhi haar mat maano", "Ek aur koshish tumhari zindagi badal sakti hai!",
         "Rukna nahi, thakna nahi,\\nApne sapnon se kabhi darna nahi.",
         ["Challenge", "Practice", "Nayi shuruaat"]),
    ],
    "Attitude": [
        ("Apni pehchaan", "Naam chahiye toh kaam aisa karo!",
         "Bheed ka hissa nahi banna,\\nApni pehchaan khud banana hai.",
         ["Confident walk", "Mehnat", "Final pose"]),
        ("Khamoshi se mehnat", "Har baat ka jawab dena zaroori nahi!",
         "Abhi khamosh hoon, kamzor nahi,\\nMera waqt aayega, bas shor nahi.",
         ["Log mazaak banate hain", "Mehnat", "Result"]),
        ("Apne dum par", "Jab koi saath na de, khud ka saath dena!",
         "Sahara mile toh achha hai,\\nPar chalna apne dum par hi hai.",
         ["Akela safar", "Mushkil raasta", "Aage badhna"]),
        ("Apna level", "Apni race mein khud ko behtar banao!",
         "Muqabla kal wale khud se hai,\\nManzil tak jaana apne dum se hai.",
         ["Planning", "Practice", "Progress"]),
    ],
    "Emotional Story": [
        ("Papa ka purana joota", "Us din bete ko papa ki mehnat samajh aayi!",
         "Beta: Papa, naya joota kyun nahi lete?\\nPapa: Pehle tere sapne poore kar loon, beta.",
         ["Purana joota", "Papa ki mehnat", "Gale lagna"]),
        ("Maa ka intezaar", "Maa aaj bhi darwaze par tumhara intezaar karti hai!",
         "Duniya kitni bhi badi ho jaaye,\\nMaa ke liye bachcha hamesha bachcha rehta hai.",
         ["Maa intezaar karti hai", "Beta ghar lautata hai", "Maa gale lagati hai"]),
        ("Ek chhoti si madad", "Ek chhoti madad kisi ki zindagi badal sakti hai!",
         "Insaan bada paison se nahi,\\nKisi ke kaam aane se banta hai.",
         ["Pareshan insaan", "Madad milti hai", "Muskurahat"]),
        ("Purani yaadein", "Kabhi-kabhi ek purani cheez bahut kuch yaad dila deti hai!",
         "Kuch yaadein dil mein rehti hain,\\nAur kuch chehre par muskaan laati hain.",
         ["Purani tasveer", "Yaad ka pal", "Emotional smile"]),
    ],
}

topic = st.selectbox("🎬 Reel ka topic chuno", list(IDEAS.keys()))
duration = st.selectbox("⏱️ Reel duration", ["10 seconds", "15 seconds", "30 seconds"])
count = st.slider("💡 Kitne ideas chahiye?", min_value=1, max_value=5, value=3)

if st.button("🚀 Mere Reel Ideas Banao", use_container_width=True):
    st.session_state["generated"] = random.sample(
        IDEAS[topic], k=min(count, len(IDEAS[topic]))
    )
    st.session_state["generated_topic"] = topic
    st.session_state["generated_duration"] = duration

if "generated" in st.session_state:
    for i, (title, hook, dialogue, scenes) in enumerate(st.session_state["generated"], start=1):
        st.divider()
        st.subheader(f"🎥 Idea {i}: {title}")
        st.markdown("**🎯 Hook — shuruaat**")
        st.write(hook)
        st.markdown("**🎬 Scene-by-scene plan**")
        for scene in scenes:
            st.write(f"• {scene}")
        st.markdown("**🗣️ Hindi dialogue / voiceover**")
        st.text(dialogue)
        st.markdown("**🏁 Ending / CTA**")
        st.write("Aisi aur videos ke liye follow karein aur apni rai comment karein.")
        st.markdown("**✍️ Caption**")
        st.write(f"{title} ❤️ Aapki kya rai hai? Comment mein zaroor batao!")
        st.markdown("**#️⃣ Hashtags**")
        st.write("#HindiReels #InstagramIndia #ReelsIdeas #DigitalCreator #HindiContent")
        st.caption(f"Suggested duration: {st.session_state.get('generated_duration', duration)}")

    if st.button("🔄 Aur naye ideas banao", use_container_width=True):
        st.session_state.pop("generated", None)
        st.rerun()

st.divider()
st.caption("Original content banao; views aur follower growth ki guarantee nahi hoti.")

