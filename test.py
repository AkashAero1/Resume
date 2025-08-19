import streamlit as st
from PIL import Image
import base64

# Set page config
st.set_page_config(
    page_title="My Professional Resume",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")  # You can create a separate CSS file for styling

# Profile image
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Replace with your image path
profile_image = "profile.jpg"  # Place your image in the same directory
image_base64 = get_image_base64(profile_image) if profile_image else None

# Sidebar
with st.sidebar:
    if image_base64:
        st.markdown(
            f'<div class="profile-img-container">'
            f'<img src="data:image/jpeg;base64,{image_base64}" class="profile-img">'
            f'</div>',
            unsafe_allow_html=True
        )
    
    st.title("Akash Sharma")
    st.markdown("**📍 Surat, Gujarat, India**")
    
    st.markdown("---")
    
    st.markdown("### Contact Info")
    st.markdown("📧email: akashrock30950@gmail.com")
    st.markdown("📞Phone No.: +91 8238423031")
    st.markdown("🔗Linkedin: https://www.linkedin.com/in/akash-sharma-305524304/")
    st.markdown("💻Github: https://github.com/AkashAero1")
    st.markdown("Codeforces: https://codeforces.com/profile/Avgeek")
    
    st.markdown("---")
    
    st.markdown("### Skills")
    st.markdown("- Python")
    st.markdown("- Machine Learning")
    st.markdown("- DSA")
    st.markdown("- N8N")
    st.markdown("- Langchain")
    st.markdown("- Langgraph")
    st.markdown("- SQL")
    st.markdown("- Streamlit")
    st.markdown("- FastApi")
    st.markdown("- Pydantic")
    st.markdown("- Codeforces")
    st.markdown("- Competitive Programming ")
    st.markdown("- Numpy ")
    st.markdown("- Pandas ")
    st.markdown("- Matplotlib ")
    st.markdown("- Seaborn ")
    st.markdown("- Plotly ")
    st.markdown("- PowerBI ")
    st.markdown("- Tableau ")
    
    st.markdown("---")

    
    # st.markdown("### Download Resume")
    # with open("resume.pdf", "rb") as pdf_file:  # Replace with your actual PDF
    #     PDFbyte = pdf_file.read()
    # st.download_button(
    #     label="Download PDF",
    #     data=PDFbyte,
    #     file_name="JohnDoe_Resume.pdf",
    #     mime="application/octet-stream"
    # )

# Main content
st.header("RESUME")
st.markdown("""
Aspiring Civil Engineering undergraduate at NIT Surat with intrests in AI, ML and Automation having strong foundations in Python, Machine Learning and Chatbots. Passionate about Entrepreneurship, seeking opportunities to apply problem-solving and technical skills in impactful projects, research, and internships.
""")

# Experience
st.header("Skills")
st.markdown("- Python")
st.markdown("- Machine Learning")
st.markdown("- DSA")
st.markdown("- N8N")
st.markdown("- Langchain")
st.markdown("- Langgraph")
st.markdown("- SQL")
st.markdown("- Streamlit")
st.markdown("- FastApi")
st.markdown("- Pydantic")
st.markdown("- Codeforces")
st.markdown("- Competitive Programming ")
st.markdown("- Numpy ")
st.markdown("- Pandas ")
st.markdown("- Matplotlib ")
st.markdown("- Seaborn ")
st.markdown("- Plotly ")
st.markdown("- PowerBI ")
st.markdown("- Tableau ")

# Projects
st.header("Projects")

# Project 1
st.subheader("AI Mental Health Checker")
st.markdown("""
Built using LangChain & Sentiment Analysis to track emotions and provide supportive responses.
            
👉 Try it live:https://lnkd.in/gxbVuwBN 
""")

st.subheader("Voice Assistant JARVIS")
st.markdown("""
Python-based voice assistant integrating speech recognition and task automation.
""")

st.subheader("StudentWell - Mental Health Support Platform")
st.markdown("""
A web platform with mood tracking, group chat, and study planning features to support student well-being.
""")




# Education
st.header("Education")
st.markdown("**National Institute of Technology (NIT), Surat**")
st.markdown("**Bachelor of Technology (B.Tech) in Civil Engineering)**")
st.markdown("**2024-2028**")



# Contact Form
st.header("Get In Touch")
contact_form = """
<form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)