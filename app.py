import streamlit as st
import os
from dotenv import load_dotenv
from utils.chatbot import MedicalChatbot

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🏥",
    layout="wide"
)

def main():
    st.title("🏥 Medical Chatbot Assistant")
    st.markdown("*Get medical information and guidance. Always consult healthcare professionals for serious concerns.*")
    
    # Initialize chatbot
    if 'chatbot' not in st.session_state:
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            st.error("Please set your Google API key in the .env file")
            st.stop()
        st.session_state.chatbot = MedicalChatbot(api_key)
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me about your health concerns..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.chatbot.get_response(prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_msg = f"Sorry, I encountered an error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
    
    # Sidebar with disclaimer
    with st.sidebar:
        st.markdown("### ⚠️ Medical Disclaimer")
        st.markdown("""
        This chatbot provides general health information only. 
        It is not a substitute for professional medical advice, 
        diagnosis, or treatment. Always consult qualified 
        healthcare providers for medical concerns.
        """)
        
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()