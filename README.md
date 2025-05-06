# JobFit-Analyzer

Welcome to **JobFit Analyzer**, an innovative application designed to enhance your resume's compatibility with Applicant Tracking Systems (ATS). In today's competitive job market, it is crucial to ensure your resume stands out and meets the specific requirements of job descriptions (JDs). JobFit Analyzer leverages advanced AI technology to analyze your resume against job descriptions, providing valuable feedback to optimize your chances of landing your dream job.

## Key Features

- **Resume Analysis**: Upload your resume in PDF format, and JobFit Analyzer will extract and analyze the text content.
- **Job Description Matching**: Input the job description, and the AI will evaluate your resume against it.
- **Detailed Feedback**: Receive a comprehensive analysis, including a percentage match score, missing keywords, and a profile summary.
- **Actionable Insights**: Get recommendations on how to improve your resume for better alignment with the job description.

## How to Use JobFit Analyzer

1. **Paste the Job Description**: Copy and paste the job description of the position you are applying for into the provided text area.
2. **Upload Your Resume**: Upload your resume in PDF format using the file uploader.
3. **Submit**: Click the "Submit" button to initiate the analysis.
4. **Review Feedback**: Once the analysis is complete, you will receive detailed feedback on how well your resume matches the job description, along with suggestions for improvement.

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- google.generativeai
- PyPDF2
- python-dotenv

### Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/jobfit-analyzer.git
    cd jobfit-analyzer
    ```

2. **Install the Required Packages**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**

    Create a `.env` file in the root directory and add your Google API key:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

### Running the Application

```sh
streamlit run app.py
