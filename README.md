# AI Speech Recognition App

## Live Demo
Try out the deployed application here:
🚀 Streamlit App → (Add your Streamlit URL here once deployed)

## Overview
This project is a simple AI-based speech-to-text application that converts spoken audio into written text using the Whisper model. The application provides an easy-to-use web interface where users can upload an audio file and receive the corresponding transcription.

## Features
- Upload audio files in `.wav`, `.mp3`, or `.m4a` format  
- Convert speech audio into text  
- Clean and minimal user interface built using Streamlit  

## Tech Stack
- Python  
- Streamlit  
- Whisper / Faster-Whisper  

## Project Structure

```text
AI-Speech-Recognition/
│
├── app.py # Streamlit UI and application logic
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── assets
│   └──Sample.mp3 # Sample audio file  
│
├── ai_engine/
│   ├── init.py
│   └── model.py # Speech-to-text model logic
│
└── screenshots/ # Application screenshots
    ├── home.png
    ├── upload.png
    └── result.png
```

## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2025-12-21 012540 copy.png>)

### Audio Upload
![Audio Upload](<screenshots/Screenshot 2025-12-21 012559.png>)

### Transcription Output
![Transcription Output](<screenshots/Screenshot 2025-12-21 012842.png>)

## How It Works
First, all the required dependencies are installed and the application is started. Once the app is running, the user is taken to a simple web interface. The user uploads an audio file using the file uploader and then clicks the Transcribe button. The uploaded audio is processed by the Whisper model, and after a short processing time, the spoken content is converted into readable text and displayed on the screen.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Run the application:
    streamlit run app.py

## Usage
This application can be useful for content creators or anyone who wants to convert audio into text. If you have an audio file and need a written transcript—such as captions for videos, notes from recordings, or documentation—you can simply upload the file and get the text output instantly.

## Future Improvements
Add live microphone input for real-time transcription
Improve accuracy using larger or more advanced models
Enhance the UI for a better user experience

## Learning Outcomes
Initially, building this project felt difficult, but once I started working step by step, the concepts began to make sense. This project helped me understand how AI models can be integrated into real applications. It also reinforced the idea that learning happens by building, experimenting, and improving over time rather than trying to know everything in advance.
