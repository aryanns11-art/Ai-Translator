🌐 Voice Translator Desktop App
A modern desktop Translator application built using Python and CustomTkinter.

This application allows users to translate text into multiple languages, convert speech to text using a microphone, and listen to translated text with text-to-speech. It provides a clean and user-friendly interface with support for several popular languages.

✨ Features
🌍 Translate text into multiple languages
🎤 Speech-to-Text using your microphone
🔊 Listen to translated text using Text-to-Speech
🎵 Audio file transcription (MP3/WAV support)
🎨 Modern GUI built with CustomTkinter
📝 Simple and clean user interface
🌐 Automatic source language detection
⚡ Fast translation using Google Translate
🎧 Audio playback using Pygame
💬 Placeholder text support
🖥️ Responsive two-panel layout

🛠️ Technologies Used
Python 3
CustomTkinter
Pillow (PIL)
deep-translator
SpeechRecognition
gTTS (Google Text-to-Speech)
Pygame
Threading
pydub
FFmpeg
Google Speech Recognition API

📦 Required Libraries
Install all dependencies before running the project.

pip install customtkinter
pip install pillow
pip install deep-translator
pip install SpeechRecognition
pip install gTTS
pip install pygame
pip install pyaudio
pip install pydub

If installing PyAudio fails on Windows:

pip install pipwin
pipwin install pyaudio

⚠️ FFmpeg is required for MP3 processing (used by pydub)

🚀 How to Run
Clone the repository

git clone https://github.com/your-username/voice-translator-python.git

Go to the project folder

cd voice-translator-python

Run the application

python main.py

🌍 Supported Languages
Spanish 🇪🇸
French 🇫🇷
German 🇩🇪
Italian 🇮🇹
Japanese 🇯🇵
Chinese (Simplified) 🇨🇳
Hindi 🇮🇳
Arabic 🇸🇦
Russian 🇷🇺

📂 Project Structure
voice-translator-python/
│
├── main.py
├── download.png
├── mic.png
├── README.md
└── requirements.txt

🎯 How It Works
Enter text manually or use the microphone.
Or select an audio file (MP3/WAV).
Select your target language.
Click Translate / Process Audio.
The translated text appears in the output panel.
Click the speaker button to hear the translated text.

📸 Features Preview
Clean Modern UI
Voice Input
Instant Translation
Audio Playback
Multi-language Support

🔮 Future Improvements
🌐 More language support
📋 Copy translated text
📄 Save translations to file
📚 Translation history
🌙 Dark mode support
🔄 Language swap button
🎙️ Continuous voice translation
📱 Better UI animations

🤝 Contributing
Contributions are welcome!

Feel free to fork this repository, improve the project, and submit a Pull Request.

📄 License
This project is open source and available under the MIT License.

👨‍💻 Author
Aryan

Diploma Computer Engineering Student

Passionate about Python, Machine Learning, AI, and Software Development.

⭐ If you like this project
Give this repository a Star ⭐ and share it with others!

---

## 🆕 Improvements

* Added audio file support (MP3/WAV)
* MP3 → WAV conversion using pydub + FFmpeg
* Language selection validation (prevents crash)
* Improved error handling (FFmpeg + speech recognition)
* Fixed textbox state issue
* Improved UI feedback during processing
* Stable threading for background tasks

---

## 🏷️ Tags

#Python #TranslatorApp #SpeechRecognition #TextToSpeech #CustomTkinter
#GUI #AI #DeepTranslator #Pydub #FFmpeg
#DesktopApp #OpenSource #VoiceTranslator
