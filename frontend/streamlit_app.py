import streamlit as st
from jinja2 import Template

# ---------------------------
# Streamlit Configuration
# ---------------------------
st.set_page_config(
    page_title="AI Resume Generator",
    page_icon="📝",
    layout="centered",
)

# Apply custom CSS for Black Theme
st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #262730;
        color: white;
        border-radius: 8px;
    }
    .stTextArea textarea {
        background-color: #262730;
        color: white;
        border-radius: 8px;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #262730;
        color: white;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Resume Generator
# ---------------------------
st.title("📝 AI-Powered Resume Generator")
st.write("Fill in your details to generate a customized resume.")

# Personal Info
st.header("👤 Personal Details")
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
location = st.text_input("Job Location (City, Country)")
linkedin = st.text_input("LinkedIn Profile URL")
portfolio = st.text_input("Portfolio / GitHub URL")

# Education
st.header("🎓 Education")
education = st.text_area("Enter your Education Details (e.g. B.Tech in CSE, XYZ University, 2020-2024)")

# Experience
st.header("💼 Work Experience")
experience = st.text_area("Enter your Work Experience (e.g. Software Engineer Intern at ABC Corp, 6 months)")

# Skills
st.header("🛠️ Skills")
skills = st.text_area("List your technical & soft skills (comma separated)")

# Job Role
st.header("🎯 Job Role")
job_role = st.selectbox("Select Target Job Role", ["Software Engineer", "Data Analyst", "AI Engineer", "Web Developer", "Other"])

# ---------------------------
# Resume Template
# ---------------------------
resume_template = """
# {{ name }}

📍 **Location:** {{ location }}  
📧 **Email:** {{ email }}  
📱 **Phone:** {{ phone }}  
🔗 [LinkedIn]({{ linkedin }}) | [Portfolio]({{ portfolio }})

---

## 🎯 Objective
Aspiring **{{ job_role }}** seeking opportunities in **{{ location }}**, bringing strong skills in problem-solving, teamwork, and innovation.

---

## 🎓 Education
{{ education }}

---

## 💼 Work Experience
{{ experience }}

---

## 🛠️ Skills
{{ skills }}
"""

# ---------------------------
# Generate Resume
# ---------------------------
if st.button("Generate Resume"):
    template = Template(resume_template)
    resume = template.render(
        name=name,
        email=email,
        phone=phone,
        location=location,
        linkedin=linkedin,
        portfolio=portfolio,
        education=education,
        experience=experience,
        skills=skills,
        job_role=job_role
    )

    st.markdown("## 📄 Your Resume")
    st.markdown(resume)

    # Save Resume to a text file
    with open("resume.txt", "w", encoding="utf-8") as f:
        f.write(resume)
    st.success("✅ Resume generated successfully! You can find it in resume.txt")
