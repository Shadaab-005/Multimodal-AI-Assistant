# Voice Interaction & Real-Time Emotion Recognition System
**A Multimodal Web Application Combining Voice Interaction & Real-Time Emotion Recognition**

[![Flask](https://img.shields.io/badge/Flask-2.3.2-000000?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![Google Generative AI](https://img.shields.io/badge/Google_Generative_AI-0.3.2-4285F4?logo=google)](https://ai.google.dev/)
[![Web Speech API](https://img.shields.io/badge/Web_Speech_API-1.0-blue)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-5C3EE8?logo=opencv)](https://opencv.org/)

![Project Demo](https://via.placeholder.com/800x400.png?text=Add+Demo+GIF+Here)

A full-stack web application integrating Google's Gemini AI for natural voice conversations and real-time emotion analysis through webcam feed, featuring dual-modal interaction history.

## Table of Contents
- [Features](##features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features ✨
- 🎤 **Voice Interaction**  
  Real-time speech-to-text conversion with Web Speech API + AI responses
- 😃 **Emotion Recognition**  
  Live webcam emotion analysis using Gemini Vision
- 💾 **Conversation History**  
  Unified log tracking both voice interactions and emotion insights
- 🔊 **Multimodal Feedback**  
  Text-to-speech responses + visual emotion analysis
- 🔒 **Secure Configuration**  
  Environment-based API key management

## Demo 🎥
*(Add screenshot/GIF of working application here)*

## Installation ⚙️

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/ai-voice-emotion-assistant.git
cd ai-voice-emotion-assistant


2\. **Set Up Virtual Environment**

```bash

python -m venv venv

source venv/bin/activate  # Linux/MacOS

venv\Scripts\activate  # Windows

```

3\. **Install Dependencies**

```bash

pip install -r requirements.txt

```

4\. **API Configuration**

```bash

echo "GOOGLE_API_KEY=your_api_key_here" > .env

```

## Usage 🚀

1\. **Start Application**

```bash

python app.py

```

2\. **Access in Browser**  

   Visit `http://localhost:5001`

3\. **Features**  

   - Click 🎤 for voice interactions

   - Click 😃 for real-time emotion analysis

   - View unified interaction history below

## Tech Stack 🛠️

**Frontend**  

| HTML5 Canvas | Web Speech API | Responsive CSS | JavaScript (ES6+) |

**Backend**  

| Python Flask | Base64 Image Processing | Session Management |

**AI/ML**  

| Google Gemini API | Multimodal Prompt Engineering | Real-time Vision Analysis |

**Tools**  

| Git | dotenv | PIL | WebRTC |

## Contributing 🤝

1\. Fork the Project

2\. Create your Feature Branch

```bash

git checkout -b feature/AmazingFeature

```

3\. Commit Changes

```bash

git commit -m 'Add some AmazingFeature'

```

4\. Push to Branch

```bash

git push origin feature/AmazingFeature

```

5\. Open Pull Request

## License 📄

Distributed under MIT License. See `LICENSE` for details.

## Acknowledgements 🙏

- Google Gemini API Team

- Flask Community

- MDN Web Docs (Web Speech API)

```

**To Use:**  

1\. Replace placeholder text (especially in API Configuration and Demo sections)  

2\. Add actual screenshots/video in the Demo section  

3\. Customize badges/colors as needed  

4\. Create a `requirements.txt` with:

```

flask==3.0.2

python-dotenv==1.0.0

google-generativeai==0.3.2

Pillow==10.1.0

```

**Key Features of this README:**  

✅ Professional visual presentation  

✅ Clear installation/usage instructions  

✅ Modular tech stack breakdown  

✅ Contribution guidelines  

✅ Responsive design elements  

✅ License/attribution compliance

Let me know if you need help creating the requirements.txt or any other components!
