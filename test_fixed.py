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
    
    st.title("John Doe")
    st.markdown("**Senior Data Scientist**")
    st.markdown("📍 San Francisco, CA")
    
    st.markdown("---")
    
    st.markdown("### Contact Info")
    st.markdown("📧 john.doe@email.com")
    st.markdown("📞 (123) 456-7890")
    st.markdown("🌐 [portfolio.com](https://www.portfolio.com)")
    st.markdown("🔗 [linkedin.com/in/johndoe](https://www.linkedin.com/in/johndoe)")
    st.markdown("💻 [github.com/johndoe](https://www.github.com/johndoe)")
    
    st.markdown("---")
    
    st.markdown("### Skills")
    st.markdown("- Python (Advanced)")
    st.markdown("- Machine Learning")
    st.markdown("- Data Analysis")
    st.markdown("- SQL")
    st.markdown("- Streamlit")
    st.markdown("- TensorFlow/PyTorch")
    st.markdown("- Cloud Computing (AWS)")
    
    st.markdown("---")
    
    st.markdown("### Download Resume")
    with open("resume.pdf", "rb") as pdf_file:  # Replace with your actual PDF
        PDFbyte = pdf_file.read()
    st.download_button(
        label="Download PDF",
        data=PDFbyte,
        file_name="JohnDoe_Resume.pdf",
        mime="application/octet-stream"
    )

# Main content
st.header("Professional Summary")
st.markdown("""
Experienced Data Scientist with 5+ years of expertise in building machine learning models, 
data analysis, and creating data-driven solutions. Passionate about leveraging data to solve 
complex problems and drive business decisions. Strong background in Python, statistical modeling, 
and cloud technologies. Excellent communicator with proven ability to collaborate across 
multidisciplinary teams.
""")

st.markdown("---")

# Experience
st.header("Work Experience")

# Job 1
st.subheader("Senior Data Scientist - TechCorp Inc.")
st.markdown("**Jan 2020 - Present | San Francisco, CA**")
st.markdown("""
- Led a team of 5 data scientists to develop predictive models that improved customer retention by 25%
- Designed and implemented a recommendation system that increased sales by 18%
- Built automated data pipelines reducing manual work by 30 hours/week
- Created interactive dashboards using Streamlit for business stakeholders
- Mentored junior team members and conducted technical training sessions
""")

# Job 2
st.subheader("Data Scientist - DataAnalytics LLC")
st.markdown("**Jun 2017 - Dec 2019 | New York, NY**")
st.markdown("""
- Developed machine learning models for customer segmentation and churn prediction
- Automated reporting processes saving 15+ hours per week
- Conducted A/B tests and presented findings to executive team
- Collaborated with engineering team to deploy models to production
""")

st.markdown("---")

# Education
st.header("Education")
st.subheader("Master of Science in Computer Science")
st.markdown("**Stanford University | 2015 - 2017**")
st.markdown("- Specialization in Artificial Intelligence")
st.markdown("- GPA: 3.8/4.0")

st.subheader("Bachelor of Science in Mathematics")
st.markdown("**University of California, Berkeley | 2011 - 2015**")
st.markdown("- Minor in Statistics")
st.markdown("- Graduated with Honors")

st.markdown("---")

# Projects
st.header("Projects")

# Project 1
st.subheader("Customer Churn Prediction System")
st.markdown("""
- Built an ensemble model (XGBoost + Random Forest) to predict customer churn with 89% accuracy
- Deployed as a REST API using FastAPI
- Integrated with company CRM system
- Resulted in $2M annual savings from reduced churn
""")

# Project 2
st.subheader("Real-time Sentiment Analysis Dashboard")
st.markdown("""
- Developed a Streamlit dashboard analyzing social media sentiment in real-time
- Used NLP techniques and BERT for sentiment classification
- Processed 10,000+ tweets per hour using AWS infrastructure
- Used by marketing team to monitor brand perception
""")

st.markdown("---")

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