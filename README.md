# 🚀 Akash's Interactive Resume Website

A modern, interactive resume website built with Streamlit featuring an AI-powered chatbot assistant.

## ✨ Features

- **Professional Design**: Modern, responsive UI with beautiful styling
- **Interactive Navigation**: Sidebar with quick access to different sections
- **AI Chatbot**: Intelligent assistant that can answer questions about the resume
- **Responsive Layout**: Optimized for all device sizes
- **Download Options**: PDF and Word document download buttons
- **Professional Sections**: Experience, Education, Skills, Projects, and Contact

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Styling**: Custom CSS with modern design principles
- **AI Chatbot**: Rule-based intelligent responses
- **Icons**: Emoji and Unicode symbols for visual appeal

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation & Setup

1. **Clone or download the project files**
   ```bash
   # If using git
   git clone <repository-url>
   cd Resume
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, manually navigate to the URL

## 🎯 How to Use

### Main Resume Sections
- **About Me**: Personal introduction and background
- **Technical Skills**: Programming languages, web technologies, and tools
- **Professional Experience**: Work history with detailed descriptions
- **Education**: Academic qualifications and degrees
- **Projects**: Notable projects with tech stack information
- **Contact Information**: Multiple ways to get in touch

### AI Chatbot
- Click the "🤖 AI Chatbot" button in the sidebar
- Ask questions about experience, skills, education, projects, or contact info
- The chatbot will provide intelligent, contextual responses

### Navigation
- Use the sidebar for quick navigation between sections
- All sections are accessible from the main page as well

## 🎨 Customization

### Personal Information
Edit the following sections in `app.py`:
- Name and title
- Contact information
- Work experience
- Education details
- Skills and technologies
- Project descriptions

### Styling
Modify the CSS in the `st.markdown` section to:
- Change colors and fonts
- Adjust spacing and layout
- Customize button styles
- Modify card designs

### AI Chatbot Responses
Update the `generate_ai_response()` function to:
- Add more question patterns
- Customize response content
- Include additional resume information

## 📱 Features Breakdown

### 1. Professional Header
- Large, prominent name display
- Professional title and subtitle
- Modern typography and colors

### 2. Skills Section
- Organized into three columns
- Color-coded skill tags
- Professional appearance

### 3. Experience Cards
- Clean, card-based layout
- Company information and duration
- Detailed role descriptions

### 4. Education Section
- Two-column layout for degrees
- Institution names and dates
- Specialization details

### 5. Project Showcase
- Project descriptions with tech stacks
- Professional presentation
- Highlighted technologies used

### 6. Contact Section
- Gradient background design
- Multiple contact methods
- Professional appearance

### 7. AI Chatbot
- Intelligent question understanding
- Contextual responses
- Professional communication style

## 🔧 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Kill existing process or use different port
   streamlit run app.py --server.port 8502
   ```

2. **Package installation errors**
   ```bash
   # Upgrade pip first
   python -m pip install --upgrade pip
   # Then install requirements
   pip install -r requirements.txt
   ```

3. **Streamlit not found**
   ```bash
   # Install streamlit globally
   pip install streamlit
   ```

## 🚀 Deployment Options

### Local Development
- Run locally for development and testing
- Access via `localhost:8501`

### Streamlit Cloud
- Deploy to Streamlit Cloud for free hosting
- Connect your GitHub repository
- Automatic updates on code changes

### Other Cloud Platforms
- Heroku
- AWS
- Google Cloud Platform
- Azure

## 📝 Future Enhancements

- [ ] Integration with external AI APIs (OpenAI, etc.)
- [ ] Database backend for dynamic content
- [ ] User authentication and admin panel
- [ ] Analytics and visitor tracking
- [ ] Multi-language support
- [ ] Dark/Light theme toggle
- [ ] PDF generation functionality
- [ ] Contact form integration

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you have any questions or need help:
- Create an issue in the repository
- Contact via the information in the resume
- Check the troubleshooting section above

---

**Made with ❤️ using Streamlit**
