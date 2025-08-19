# Configuration file for the resume website
# Modify these values to customize your resume

# Personal Information
PERSONAL_INFO = {
    "name": "Akash",
    "title": "Software Developer & AI Enthusiast",
    "location": "India",
    "email": "akash@example.com",
    "phone": "+91 98765 43210",
    "linkedin": "linkedin.com/in/akash",
    "github": "github.com/akash"
}

# About Me Section
ABOUT_ME = """
I am a passionate software developer with expertise in modern web technologies, 
machine learning, and artificial intelligence. I love creating innovative solutions 
that solve real-world problems and enhance user experiences.

My journey in technology has been driven by curiosity and a desire to learn new things. 
I believe in writing clean, maintainable code and staying updated with the latest industry trends.
"""

# Technical Skills
SKILLS = {
    "Programming Languages": ["Python", "JavaScript", "Java", "C++", "SQL"],
    "Web Technologies": ["HTML/CSS", "React", "Node.js", "Django", "Flask"],
    "Tools & Platforms": ["Git", "Docker", "AWS", "Azure", "Streamlit"],
    "AI/ML": ["TensorFlow", "Scikit-learn", "NLP", "Computer Vision"]
}

# Professional Experience
EXPERIENCE = [
    {
        "title": "Senior Software Developer",
        "company": "Tech Solutions Inc.",
        "duration": "2022 - Present",
        "description": "Led development of scalable web applications using React and Node.js. Implemented CI/CD pipelines and mentored junior developers."
    },
    {
        "title": "Software Developer",
        "company": "Innovation Labs",
        "duration": "2020 - 2022",
        "description": "Developed RESTful APIs and microservices. Worked on machine learning projects and data analysis tools."
    },
    {
        "title": "Junior Developer",
        "company": "StartUp Hub",
        "duration": "2019 - 2020",
        "description": "Built responsive web applications and contributed to agile development processes."
    }
]

# Education
EDUCATION = [
    {
        "degree": "Master's in Computer Science",
        "institution": "University of Technology",
        "duration": "2019 - 2021",
        "description": "Specialized in Artificial Intelligence and Machine Learning"
    },
    {
        "degree": "Bachelor's in Computer Science",
        "institution": "Engineering College",
        "duration": "2015 - 2019",
        "description": "Computer Science and Engineering"
    }
]

# Projects
PROJECTS = [
    {
        "title": "AI-Powered Resume Parser",
        "description": "Built an intelligent system that automatically extracts and categorizes information from resumes using NLP and machine learning.",
        "tech_stack": "Python, TensorFlow, Streamlit, NLTK"
    },
    {
        "title": "E-commerce Platform",
        "description": "Developed a full-stack e-commerce solution with user authentication, payment integration, and admin dashboard.",
        "tech_stack": "React, Node.js, MongoDB, Stripe"
    },
    {
        "title": "Data Analysis Dashboard",
        "description": "Created interactive dashboards for business intelligence and data visualization using Python and modern web technologies.",
        "tech_stack": "Python, Plotly, Dash, Pandas"
    }
]

# AI Chatbot Responses
CHATBOT_RESPONSES = {
    "experience": """I have over 4 years of experience in software development:

• **Senior Software Developer** at Tech Solutions Inc. (2022-Present)
• **Software Developer** at Innovation Labs (2020-2022)  
• **Junior Developer** at StartUp Hub (2019-2020)

I've worked on web applications, APIs, microservices, and machine learning projects.""",

    "skills": """My technical skills include:

**Programming Languages:** Python, JavaScript, Java, C++, SQL
**Web Technologies:** HTML/CSS, React, Node.js, Django, Flask
**Tools & Platforms:** Git, Docker, AWS, Azure, Streamlit
**AI/ML:** TensorFlow, Scikit-learn, NLP, Computer Vision""",

    "education": """My educational background:

• **Master's in Computer Science** from University of Technology (2019-2021)
  - Specialized in AI and Machine Learning
• **Bachelor's in Computer Science** from Engineering College (2015-2019)""",

    "projects": """Some of my notable projects:

• **AI-Powered Resume Parser** - Built with Python, TensorFlow, and NLP
• **E-commerce Platform** - Full-stack solution with React, Node.js, MongoDB
• **Data Analysis Dashboard** - Interactive BI tools with Python and Plotly""",

    "contact": f"""You can reach me at:

📧 Email: {PERSONAL_INFO['email']}
📱 Phone: {PERSONAL_INFO['phone']}
🌐 LinkedIn: {PERSONAL_INFO['linkedin']}
🐙 GitHub: {PERSONAL_INFO['github']}""",

    "greeting": "Hello! 👋 I'm Akash's AI assistant. I can help you learn more about my experience, skills, education, projects, or contact information. What would you like to know?",

    "default": """I'm not sure I understand your question. You can ask me about:

• My work experience and background
• Technical skills and technologies I use
• Education and qualifications
• Projects I've worked on
• How to contact me

Feel free to rephrase your question!"""
}

# Page Configuration
PAGE_CONFIG = {
    "page_title": "Akash's Resume",
    "page_icon": "📄",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Color Scheme
COLORS = {
    "primary": "#1f77b4",
    "secondary": "#2c3e50",
    "accent": "#3498db",
    "success": "#27ae60",
    "text_light": "#7f8c8d",
    "text_dark": "#2c3e50",
    "background_light": "#f8f9fa",
    "gradient_start": "#667eea",
    "gradient_end": "#764ba2"
}
