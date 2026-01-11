# 🏥 Medical Chatbot

A medical assistant chatbot built with Streamlit and Google Gemini API that provides general health information and guidance.

## ⚠️ Medical Disclaimer

This chatbot provides general health information only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare providers for medical concerns.

## Features

- Interactive chat interface
- Google Gemini AI integration
- Chat history
- Medical disclaimer and safety guidelines
- Clean, responsive UI

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd medical-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Get your Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

3. Add your API key to `.env`:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment on Streamlit Cloud

1. Push your code to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Add your `GOOGLE_API_KEY` in the Streamlit Cloud secrets management:
   - Go to your app settings
   - Add secrets in TOML format:
     ```toml
     GOOGLE_API_KEY = "your_api_key_here"
     ```
5. Deploy the app

## Project Structure

```
medical-chatbot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .gitignore        # Git ignore file
├── README.md         # This file
└── utils/
    └── chatbot.py    # Chatbot logic and API integration
```

## Usage

1. Open the application in your browser
2. Type your health-related questions in the chat input
3. The chatbot will provide helpful information and guidance
4. Use the "Clear Chat History" button to start a new conversation

## Important Notes

- Always consult healthcare professionals for serious medical concerns
- This tool is for informational purposes only
- Keep your API key secure and never commit it to version control