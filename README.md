# 🌐 Voice Translator Desktop App

A modern desktop Translator application built using **Python** and **CustomTkinter**.

This application allows users to translate text into multiple languages, convert speech to text using a microphone or audio files, and listen to translated text with text-to-speech. It provides a clean and user-friendly interface with support for several popular languages.

---

# ✨ Features

* 🌍 Translate text into multiple languages
* 🎤 Speech-to-Text using your microphone
* 🎵 Audio File Transcription (MP3/WAV)
* 🔊 Listen to translated text using Text-to-Speech
* 🎨 Modern GUI built with CustomTkinter
* 📝 Simple and clean user interface
* 🌐 Automatic source language detection
* ⚡ Fast translation using Google Translate
* 🎧 Audio playback using Pygame
* 💬 Placeholder text support
* 🖥️ Responsive two-panel layout

---

# 🛠️ Technologies Used

* Python 3
* CustomTkinter
* Pillow (PIL)
* deep-translator
* SpeechRecognition
* gTTS (Google Text-to-Speech)
* Pygame
* Threading
* pydub
* FFmpeg
* Google Speech Recognition API

---

# 📦 Required Libraries

Install all dependencies before running the project.

```bash
pip install customtkinter
pip install pillow
pip install deep-translator
pip install SpeechRecognition
pip install gTTS
pip install pygame
pip install pyaudio
pip install pydub
```

If installing **PyAudio** fails on Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

**Note:** FFmpeg is required for MP3 processing with **pydub**.

---

# 🚀 How to Run

Clone the repository

```bash
git clone https://github.com/your-username/voice-translator-python.git
```

Go to the project folder

```bash
cd voice-translator-python
```

Run the application

```bash
python main.py
```

---

# 🌍 Supported Languages

* Spanish 🇪🇸
* French 🇫🇷
* German 🇩🇪
* Italian 🇮🇹
* Japanese 🇯🇵
* Chinese (Simplified) 🇨🇳
* Hindi 🇮🇳
* Arabic 🇸🇦
* Russian 🇷🇺

---

# 📂 Project Structure

```text
voice-translator-python/
│
├── main.py
├── download.png
├── mic.png
├── README.md
└── requirements.txt
```

---

# 🎯 How It Works

1. Enter text manually or use the microphone.
2. Or select an audio file (MP3/WAV).
3. Select your target language.
4. Click **Translate** or **Process Audio**.
5. The translated text appears in the output panel.
6. Click the speaker button to hear the translated text.

---

# 📸 Features Preview

* Clean Modern UI
* Voice Input
* Audio File Transcription
* Instant Translation
* Audio Playback
* Multi-language Support

---

# 🆕 Improvements

* 🎵 Added audio file transcription (MP3/WAV)
* 🔄 Automatic MP3 → WAV conversion using pydub + FFmpeg
* ✅ Language selection validation to prevent crashes
* ⚠️ Improved FFmpeg and Speech Recognition error handling
* 📝 Fixed textbox state management
* 💡 Better UI feedback while processing
* 🧵 Stable background threading for smoother performance

---

# 🔮 Future Improvements

* 🌐 More language support
* 📋 Copy translated text
* 📄 Save translations to file
* 📚 Translation history
* 🌙 Dark mode support
* 🔄 Language swap button
* 🎙️ Continuous voice translation
* 📱 Better UI animations

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository, improve the project, and submit a Pull Request.

---

# 📄 License

This project is open source and available under the MIT License.

---

# 👨‍💻 Author

**Aryan**

Diploma Computer Engineering Student

Passionate about Python, Machine Learning, AI, and Software Development.

---

## ⭐ If you like this project

Give this repository a **Star ⭐** and share it with others!

---

# 🏷️ Tags

#Python #TranslatorApp #SpeechRecognition #TextToSpeech #CustomTkinter #GUI #AI #DeepTranslator #Pydub #FFmpeg #DesktopApp #OpenSource #VoiceTranslator
