import google.generativeai as genai

class MedicalChatbot:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.system_prompt = """
        You are a helpful medical assistant chatbot. Provide accurate, helpful medical information 
        while being empathetic and professional. Always remind users to consult healthcare 
        professionals for serious concerns or emergencies. Keep responses concise but informative.
        
        Important guidelines:
        - Never provide specific diagnoses
        - Always recommend consulting healthcare professionals for serious symptoms
        - Provide general health information and guidance
        - Be empathetic and supportive
        - If asked about emergencies, advise immediate medical attention
        """
    
    def get_response(self, user_input):
        try:
            # Combine system prompt with user input
            full_prompt = f"{self.system_prompt}\n\nUser: {user_input}\nAssistant:"
            
            # Generate response
            response = self.model.generate_content(full_prompt)
            return response.text
            
        except Exception as e:
            raise Exception(f"Failed to get response from Gemini API: {str(e)}")