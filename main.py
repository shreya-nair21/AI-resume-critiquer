import streamlit as st
import PyPDF2
import io
import os
import google.generativeai as genai

# Load environment variables


# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up Streamlit UI
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")
st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback using Google's Gemini API.")

# File upload and job role input
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are targeting (optional)")
analyze = st.button("Analyze Resume")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None

# Function to extract text from either PDF or TXT
def extract_text_from_file(uploaded_file):
    try:
        if uploaded_file.type == "application/pdf":
            return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
        else:
            return uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")
        return None

# Function to analyze resume with Gemini
def analyze_resume_with_gemini(resume_text, job_role=None):
    try:
        # Initialize Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create a comprehensive prompt
        job_context = f" for the role of {job_role}" if job_role else ""
        
        prompt = f"""
        Please analyze the following resume{job_context} and provide detailed feedback in the following format:

        **STRENGTHS:**
        - List 3-4 key strengths of this resume

        **AREAS FOR IMPROVEMENT:**
        - List 3-4 specific areas that need improvement

        **SUGGESTIONS:**
        - Provide actionable recommendations to enhance the resume

        **OVERALL SCORE:** 
        - Rate the resume out of 10 and explain the rating

        **KEY RECOMMENDATIONS:**
        - Top 3 priority changes to make

        Resume Content:
        {resume_text}
        
        Please be specific, constructive, and professional in your feedback.
        """
        
        # Generate response
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"Error analyzing resume: {str(e)}"

# Handle analysis
if analyze and uploaded_file:
    # Check if API key is available
    if not os.getenv("GEMINI_API_KEY"):
        st.error("❌ Gemini API key not found. Please check your .env file.")
        st.stop()
    
    with st.spinner("Extracting text from your resume..."):
        file_content = extract_text_from_file(uploaded_file)
    
    if not file_content:
        st.error("❌ Could not extract text from the uploaded file.")
        st.stop()
    
    if not file_content.strip():
        st.error("❌ The uploaded file appears to be empty or has no readable content.")
        st.stop()
    
    # Show extracted text preview (optional)
    with st.expander("📄 Preview of extracted text"):
        st.text_area("Extracted content:", file_content[:500] + "..." if len(file_content) > 500 else file_content, height=200)
    
    with st.spinner("Analyzing your resume with AI..."):
        analysis = analyze_resume_with_gemini(file_content, job_role)
    
    # Display results
    st.markdown("### 📝 Analysis Results")
    st.markdown(analysis)
    
    # Add download option for the analysis
    st.download_button(
        label="📥 Download Analysis",
        data=analysis,
        file_name="resume_analysis.txt",
        mime="text/plain"
    )

elif analyze and not uploaded_file:
    st.warning("⚠️ Please upload a resume file first.")

# Add footer with information
st.markdown("---")
st.markdown("### 💡 Tips for better results:")
st.markdown("""
- Ensure your resume is clearly formatted
- Include specific job role for targeted feedback
- Make sure all text is readable (avoid images of text)
- Consider privacy when uploading sensitive information
""")
