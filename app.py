import google.generativeai as genai
import os
import base64
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure Google Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing from .env file")
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize models
emotion_model = genai.GenerativeModel("models/gemini-2.0-flash")
voice_model = genai.GenerativeModel("models/gemini-2.0-flash")

# Global conversation history
conversation_history = []

def process_emotion(image_data):
    try:
        # Handle different base64 formats
        if 'base64,' in image_data:
            _, data = image_data.split('base64,', 1)
        else:
            data = image_data
            
        # Decode base64 data
        image_bytes = base64.b64decode(data)
        
        # Convert to PIL Image
        image = Image.open(BytesIO(image_bytes))
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        prompt = "Analyze the emotions conveyed by the person in this image and respond directly to them, using 'you' in a short and empathetic way."
        response = emotion_model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        logging.error(f"Emotion processing error: {str(e)}")
        return f"Error processing emotion: {str(e)}"

def process_voice_input(user_input):
    try:
        prompt = f"""You are an AI assistant in an engaging conversation. The user just asked:
        '{user_input}'
        Provide a clear and concise response while keeping the conversation engaging."""
        response = voice_model.generate_content(prompt)
        return response.text
    except Exception as e:
        logging.error(f"Voice processing error: {str(e)}")
        return "Error processing voice input"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_voice', methods=['POST'])
def handle_voice():
    try:
        user_input = request.json.get('user_input')
        response = process_voice_input(user_input)
        conversation_history.append({
            'type': 'voice',
            'user': user_input,
            'ai': response,
            'timestamp': datetime.now().isoformat()
        })
        return jsonify({
            'status': 'success',
            'response': response,
            'conversation_history': conversation_history
        })
    except Exception as e:
        logging.error(f"Voice endpoint error: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/process_emotion', methods=['POST'])
def handle_emotion():
    try:
        image_data = request.json.get('image')
        response = process_emotion(image_data)
        conversation_history.append({
            'type': 'emotion',
            'ai': response,
            'timestamp': datetime.now().isoformat()
        })
        return jsonify({
            'status': 'success',
            'response': response,
            'conversation_history': conversation_history
        })
    except Exception as e:
        logging.error(f"Emotion endpoint error: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)