
import streamlit as st
import random
from datetime import datetime

# =====================================
# DEEPAK AI STUDIO - VERSION 1
# =====================================

st.set_page_config(
    page_title="DEEPAK AI STUDIO",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- DARK BLUE DESIGN ----------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #050914, #0a1530);
    color: #ffffff;
}
[data-testid="stSidebar"] {
    background: #080f20;
    border-right: 1px solid #163c70;
}
h1, h2, h3 {
    color: #55b7ff !important;
}
p, label, span {
    color: #e2eaff;
}
.stButton>button {
    background: linear-gradient(90deg,#087cff,#00c6ff);
    color: white;
    border: 0;
    border-radius: 12px;
    font-weight: bold;
    min-height: 43px;
    width: 100%;
}
.stButton>button:hover {
    border: 1px solid #ffffff;
    color: white;
}
[data-testid="stMetric"] {
    background: #101e38;
    border: 1px solid #17477e;
    padding: 15px;
    border-radius: 14px;
}
.stTextArea textarea, .stTextInput input {
    background: #101e38 !important;
    color: white !important;
}
div[data-baseweb="select"] > div {
    background: #101e38;
    color: white;
}
.card {
    background: linear-gradient(145deg,#101e38,#0a1429);
    border: 1px solid #164477;
    padding: 18px;
    border-radius: 16px;
    margin-bottom: 12px;
}
.small {
    color: #9cbce5;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION DATA ----------

if "projects" not in st.session_state:
    st.session_state.projects = []

if "last_script" not in st.session_state:
    st.session_state.last_script = ""

if "last_ideas" not in st.session_state:
    st.session_state.last_ideas = []

# ---------- HEADER ----------

st.markdown("""
<div style="text-align:center;padding:18px 5px;">
<h1>⚡ DEEPAK AI STUDIO</h1>
<p style="color:#8fcaff;">
YOUR PERSONAL AI CREATIVE STUDIO
</p>
<p style="color:#6689b8;font-size:13px;">
Create • Imagine • Generate • Inspire
</p>
</div>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------

st.sidebar.markdown("# ⚡ DEEPAK AI")
st.sidebar.caption("AI CREATIVE STUDIO")
page = st.sidebar.radio(
    "MAIN MENU",
    [
        "🏠 Home",
        "✍️ AI Script",
        "🎬 Video Studio",
        "🖼️ Image Prompt",
        "🎙️ AI Voiceover",
        "📁 My Projects",
        "ℹ️ About"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("V1.0 | Free Starter Edition")
st.sidebar.caption("Made with ❤️ by Deepak")

# ---------- HELPER ----------

def save_project(title, content, category):
    st.session_state.projects.append({
        "title": title,
        "content": content,
        "category": category,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M")
    })

# =====================================
# HOME
# =====================================

if page == "🏠 Home":

    st.subheader("👋 Welcome to your AI Studio")
    st.write("अपना अगला Creative Project यहाँ से शुरू करें।")

    c1, c2, c3 = st.columns(3)
    c1.metric("AI Tools", "5")
    c2.metric("My Projects", len(st.session_state.projects))
    c3.metric("Version", "1.0")

    st.markdown("### 🚀 CREATE SOMETHING AMAZING")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🎬 AI Video Studio</h3>
        <p>वीडियो की स्क्रिप्ट, सीन और AI Prompts तैयार करें।</p>
        <p class="small">Text • Storyboard • Video Prompts</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>✍️ AI Script Writer</h3>
        <p>Hindi Reels और YouTube के लिए स्क्रिप्ट।</p>
        <p class="small">Stories • Motivation • Technology</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🖼️ AI Image Prompt</h3>
        <p>AI Image Generator के लिए शानदार Prompts।</p>
        <p class="small">Portrait • Cinematic • 3D</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>🎙️ AI Voiceover</h3>
        <p>हिंदी Voiceover के लिए टेक्स्ट तैयार करें।</p>
        <p class="small">Hindi • Emotional • Professional</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("शुरुआत करने के लिए बाईं तरफ से कोई AI Tool चुनें।")

# =====================================
# AI SCRIPT
# =====================================

elif page == "✍️ AI Script":

    st.header("✍️ AI Script Generator")
    st.write("अपनी वीडियो के लिए हिंदी स्क्रिप्ट तैयार करें।")

    topic = st.text_input(
        "वीडियो का Topic",
        placeholder="जैसे: सफलता का रहस्य"
    )

    category = st.selectbox(
        "Category",
        ["Motivation", "Technology", "Hindi Story",
         "Comedy", "Education", "Instagram Growth"]
    )

    duration = st.selectbox(
        "वीडियो की अवधि",
        ["30 Seconds", "60 Seconds", "90 Seconds", "3 Minutes"]
    )

    if st.button("✨ Generate Hindi Script"):
        if topic.strip():
            script = f"""
TITLE: {topic}

CATEGORY: {category}
DURATION: {duration}

🎬 HOOK:
क्या आप जानते हैं {topic} के बारे में एक खास बात?

🎬 SCENE 1:
Visual: Cinematic opening animation.
Voiceover: आज हम बात करेंगे {topic} के बारे में।

🎬 SCENE 2:
Visual: Main topic के शानदार visuals.
Voiceover: मेहनत, समझ और सही जानकारी सफलता की असली कुंजी है।

🎬 SCENE 3:
Visual: Dynamic text animation.
Voiceover: इस बात को हमेशा याद रखिए और अपने लक्ष्य की तरफ आगे बढ़ते रहिए।

🎬 ENDING:
Visual: DEEPAK AI STUDIO 3D Logo.
Voiceover: वीडियो पसंद आए तो Follow और Subscribe जरूर करें।
"""
            st.session_state.last_script = script
            save_project(topic, script, "Hindi Script")
        else:
            st.warning("पहले Topic लिखें।")

    if st.session_state.last_script:
        st.text_area(
            "आपकी तैयार स्क्रिप्ट",
            value=st.session_state.last_script,
            height=300
        )

        st.download_button(
            "⬇️ Download Script",
            data=st.session_state.last_script,
            file_name="deepak_ai_script.txt",
            mime="text/plain"
        )

# =====================================
# VIDEO STUDIO
# =====================================

elif page == "🎬 Video Studio":

    st.header("🎬 AI Video Studio")
    st.write("वीडियो बनाने के लिए अपना Concept तैयार करें।")

    video_text = st.text_area(
        "वीडियो का Description लिखें",
        placeholder="जैसे: भविष्य का भारत, उड़ती हुई कारें..."
    )

    video_style = st.selectbox(
        "Video Style",
        [
            "Cinematic",
            "Motion Graphics",
            "3D Animation",
            "Realistic",
            "Documentary",
            "3D Typography"
        ]
    )

    video_duration = st.selectbox(
        "Video Duration",
        ["10 Seconds", "30 Seconds", "60 Seconds"]
    )

    video_ratio = st.selectbox(
        "Aspect Ratio",
        ["9:16 - Reels / Shorts", "16:9 - YouTube", "1:1 - Square"]
    )

    if st.button("🎥 Create Video Plan"):
        if video_text.strip():
            plan = f"""
DEEPAK AI STUDIO - VIDEO PLAN

CONCEPT:
{video_text}

STYLE: {video_style}
DURATION: {video_duration}
RATIO: {video_ratio}

SCENE 1 - INTRO:
Visual: Cinematic opening shot.
Prompt: {video_text}, professional cinematic lighting.

SCENE 2 - MAIN:
Visual: Show the main concept with dynamic camera movement.
Prompt: {video_text}, detailed animation, smooth movement.

SCENE 3 - ENDING:
Visual: DEEPAK AI STUDIO glowing blue 3D logo.
Prompt: Professional blue neon typography,
dark background, cinematic ending.

NOTE:
यह Video Plan और AI Prompts हैं।
यह फीचर अभी असली MP4 वीडियो नहीं बनाता।
"""
            st.session_state.last_ideas = [plan]
            save_project("Video: " + video_text, plan, "Video Plan")
        else:
            st.warning("वीडियो का Description लिखें।")

    for plan in st.session_state.last_ideas:
        st.text_area("Generated Video Plan", value=plan, height=330)
        st.download_button(
            "⬇️ Download Video Plan",
            data=plan,
            file_name="video_plan.txt",
            mime="text/plain",
            key="video_download"
        )

    st.info("अगले Version में वास्तविक AI Video Generation जोड़ा जाएगा।")

# =====================================
# IMAGE PROMPT
# =====================================

elif page == "🖼️ Image Prompt":

    st.header("🖼️ AI Image Prompt Generator")

    subject = st.text_input(
        "Image में क्या बनाना है?",
        placeholder="जैसे: पहाड़ पर खड़ा एक व्यक्ति"
    )

    style = st.selectbox(
        "Image Style",
        ["8K Photorealistic", "3D Art", "Cinematic",
         "Anime", "Portrait", "Fantasy"]
    )

    ratio = st.selectbox(
        "Image Ratio",
        ["9:16", "16:9", "1:1", "4:5"]
    )

    if st.button("🪄 Generate Image Prompt"):
        if subject.strip():
            prompt = f"""
Create a {style} image of {subject}.

Professional composition,
beautiful lighting, ultra detailed,
high quality, sharp focus.

Aspect ratio: {ratio}
Style: {style}
"""
            st.text_area("Your Image Prompt", value=prompt, height=180)
            save_project("Image: " + subject, prompt, "Image Prompt")
        else:
            st.warning("Subject लिखें।")

# =====================================
# AI VOICEOVER
# =====================================

elif page == "🎙️ AI Voiceover":

    st.header("🎙️ Hindi Voiceover Studio")

    voice_text = st.text_area(
        "अपना Voiceover Text लिखें",
        placeholder="नमस्कार दोस्तों, स्वागत है आपका..."
    )

    voice_style = st.selectbox(
        "Voice Style",
        ["Professional", "Emotional", "Motivational",
         "Storytelling", "Energetic"]
    )

    if st.button("🎤 Prepare Voiceover"):
        if voice_text.strip():
            output = f"""
VOICEOVER SCRIPT

STYLE: {voice_style}

TEXT:
{voice_text}

VOICE DIRECTION:
Speak in clear Hindi.
Use natural pronunciation.
Style: {voice_style}.
"""
            st.text_area("Voiceover Ready", value=output, height=200)
            st.download_button(
                "⬇️ Download Voice Text",
                data=output,
                file_name="voiceover.txt",
                mime="text/plain"
            )
            save_project("Voiceover", output, "Voiceover")
        else:
            st.warning("पहले Text लिखें।")

    st.info("यह Version Voiceover Script तैयार करता है, अभी ऑडियो फाइल नहीं बनाता।")

# =====================================
# MY PROJECTS
# =====================================

elif page == "📁 My Projects":

    st.header("📁 My Projects")

    if st.session_state.projects:
        for i, project in enumerate(reversed(st.session_state.projects)):
            with st.expander(
                f"{project['title']} | {project['category']} | {project['date']}"
            ):
                st.text(project["content"])
                st.download_button(
                    "Download",
                    data=project["content"],
                    file_name=f"project_{i}.txt",
                    mime="text/plain",
                    key=f"project_{i}"
                )
    else:
        st.info("अभी कोई Project नहीं है। पहले कोई AI Tool इस्तेमाल करें।")

    if st.session_state.projects:
        if st.button("Clear All Projects"):
            st.session_state.projects = []
            st.rerun()

# =====================================
# ABOUT
# =====================================

elif page == "ℹ️ About":

    st.header("ℹ️ About DEEPAK AI STUDIO")

    st.markdown("""
    <div class="card">
    <h2>DEEPAK AI STUDIO ⚡</h2>
    <p>Your Personal AI Creative Studio.</p>
    <p>यह प्लेटफॉर्म Content Creators के लिए बनाया जा रहा है।</p>
    <p>हमारा उद्देश्य AI की मदद से वीडियो, फोटो,
    स्क्रिप्ट और Voiceover बनाना आसान करना है।</p>
    <p class="small">Version: 1.0 Free Starter</p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("Created by Deepak | India 🇮🇳")

# ---------- FOOTER ----------

st.markdown("---")
st.markdown(
    "<center style='color:#6995c7;'>"
    "⚡ DEEPAK AI STUDIO | Create Your Imagination"
    "</center>",
    unsafe_allow_html=True
    )
            

