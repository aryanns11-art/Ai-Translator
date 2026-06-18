import customtkinter as ctk
from PIL import Image, ImageDraw
from deep_translator import GoogleTranslator
import speech_recognition as sr
from gtts import gTTS
import threading
import pygame
import os
import time
from pydub import AudioSegment
from tkinter import filedialog


recogizer = sr.Recognizer()
pygame.mixer.init()

def make_circle(img_path, size=(40, 40)):
    img = Image.open(img_path).convert("RGBA")
    img = img.resize(size)

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)

    result = Image.new("RGBA", size)
    result.paste(img, (0, 0), mask)

    return result


LANGUAGES = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN",
    "Hindi": "hi",
    "Arabic": "ar",
    "Russian": "ru"
}

class translator(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Translator")
        self.geometry("600x600")

        self.framess()
        self.selected_file_path = ""

    def clear_placeholder(self, event):
        text = self.input_box.get("0.0", "end").strip()
        if text == self.placeholder:
            self.input_box.delete("0.0", "end")
            self.input_box.configure(text_color="white")


    def add_placeholder(self, event):
        text = self.input_box.get("0.0", "end").strip()
        if not text:
            self.input_box.insert("0.0", self.placeholder)
            self.input_box.configure(text_color="gray")

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Select an Audio File",
            filetypes=[("Audio Files", "*.mp3 *.wav"), ("All Files", "*.*")]
        )
        if file_path:
            self.selected_file_path = file_path
            filename = os.path.basename(file_path)
            self.file_label.configure(text=filename, text_color="white")
    
    def start_processing(self):
        if not self.selected_file_path:
            self.file_label.configure(text="Please select a file first!", text_color="#dc3545")
            return
        threading.Thread(target=self.process_audio_logic, daemon=True).start()

    def process_audio_logic(self):
        self.trans_btn.configure(text="Processing Audio...", state="disabled")
        recognizer = sr.Recognizer()
        temp_wav_path = "converted_temp.wav"
        target_file = self.selected_file_path

        try:
            # 1. MP3 To WAV Conversion handling via pydub
            if self.selected_file_path.lower().endswith(".mp3"):
                self.trans_btn.configure(text="Converting MP3 to WAV...")
                sound = AudioSegment.from_mp3(self.selected_file_path)
                sound.export(temp_wav_path, format="wav")
                target_file = temp_wav_path

            # 2. Audio File Transcription
            self.trans_btn.configure(text="Transcribing Speech...")
            with sr.AudioFile(target_file) as source:
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.record(source)
            
            original_text = recognizer.recognize_google(audio_data)
            self.update_text_box(self.input_box, original_text, disable=False)
            

            # 3. Text Translation
            self.trans_btn.configure(text="Translating Text...")
            target_lang_name = self.lang_dropdown.get()
            target_code = LANGUAGES[target_lang_name]
            
            translated_text = GoogleTranslator(source='auto', target=target_code).translate(original_text)
            self.update_text_box(self.output_box, translated_text, disable=True)

        except sr.UnknownValueError:
            self.update_text_box(self.input_box, "Error: Engine could not decipher audio speech.")
            
        except Exception as e:
            if "ffmpeg" in str(e).lower():
                self.update_text_box(self.input_box, "FFmpeg not found! Install FFmpeg to process MP3 files.", disable=False)
            else:
                self.update_text_box(self.input_box, f"Error: {str(e)}", disable=False)
    
        finally:
            # Clean up the temporary wav translation file if it was generated
            if os.path.exists(temp_wav_path):
                try:
                    os.remove(temp_wav_path)
                except:
                    pass
            self.trans_btn.configure(text="🔄 Transcribe & Translate", state="normal")

#-----------------------------------------------------------------------------------------------------------------------

    def framess(self):

        top_label = ctk.CTkLabel(self,text="🌐 My Translator",font=ctk.CTkFont(family="Segoe UI",size=24))
        top_label.pack(anchor='nw',pady=5)
    
        #---------------------------Button Frame--------------------------------------------------------

        self.button_frame = ctk.CTkFrame(self,height=70,fg_color="#e6f2ff")
        self.button_frame.pack(fill='x',pady=2)
        self.button_frame.pack_propagate(False)
        
        self.trans_btn = ctk.CTkButton(self.button_frame,text="Translate",corner_radius=10,height=40,font=ctk.CTkFont(size=14, weight="bold"),fg_color="#2D7CC1",hover_color="#1F5F99",command=self.translate)
        self.trans_btn.pack(side='left',padx=5,pady=3)

        self.img = ctk.CTkImage(light_image=make_circle("download.png"), size=(30, 30))
        self.listen_btn = ctk.CTkButton(self.button_frame,image=self.img,text="",fg_color="#2D7CC1",hover_color="#1F5F99",command=self.start_speaking)
        self.listen_btn.pack(side='left',padx=5,pady=3)

        self.img2 =  ctk.CTkImage(light_image=make_circle("mic.png"),size=(30,30))
        self.speak_btn = ctk.CTkButton(self.button_frame,image=self.img2,text="",fg_color="#2D7CC1",hover_color="#1F5F99",command=self.speak_text)
        self.speak_btn.pack(side='left',padx=5,pady=3)

        self.lang_var = ctk.StringVar(value="Select Language")
        self.lang_dropdown = ctk.CTkOptionMenu(self.button_frame,values=['Select Language'] + list(LANGUAGES.keys()),variable=self.lang_var,width=180,height=40,corner_radius=10)
        self.lang_dropdown.pack(side='right',padx=5,pady=3)

        #----------------------- Main frame-----------------------------------------------
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Divide into 2 equal columns
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        
        self.main_frame.grid_rowconfigure(0, weight=1)

        #-------------------------------Left section---------------------------------------------------------------------------
        self.left_frame = ctk.CTkFrame(self.main_frame,fg_color="transparent",border_width=2,border_color="#87CEFA")
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        
        #------------------------------Right section---------------------------------------------------------------------------
        self.right_frame = ctk.CTkFrame(self.main_frame,fg_color="transparent",border_width=2,border_color="#87CEFA")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

        #-------------------------------TextBoxes---------------------------------------------------------------------------------
        
        self.input_box_label = ctk.CTkLabel(self.left_frame,text=" Raw Text",font=ctk.CTkFont(size=14, weight="bold"))
        self.input_box_label.pack(anchor='nw',pady=2)

        self.placeholder = "Enter text to translate..."
        
        self.input_box = ctk.CTkTextbox(self.left_frame,corner_radius=10,border_width=2)
        self.input_box.pack(fill="both",expand=True,padx=5,pady=5)

        
        self.input_box.insert("0.0", self.placeholder)
        self.input_box.configure(text_color="gray")
        
        self.input_box.bind("<FocusIn>", self.clear_placeholder)
        self.input_box.bind("<FocusOut>", self.add_placeholder)
        
        self.output_box_label = ctk.CTkLabel(self.right_frame,text=" Translated Text",font=ctk.CTkFont(size=14, weight="bold"))
        self.output_box_label.pack(anchor='nw',pady=2)
        
        self.output_box = ctk.CTkTextbox(self.right_frame,corner_radius=10,border_width=2)
        self.output_box.pack(fill="both", expand=True, padx=5, pady=5)

        self.output_box.insert("0.0", "Translated Text appears here..")
        self.output_box.configure(state="disabled")

        #---------------------------- Bottom FRame--------------------------------

        self.bottom_frame = ctk.CTkFrame(self, fg_color="#e6f2ff")
        self.bottom_frame.pack(fill="x", pady=5)

        self.file_btn = ctk.CTkButton(self.bottom_frame, text="Select Audio", command=self.browse_file)
        self.file_btn.pack(side='left', padx=5)

        self.process_audio_btn = ctk.CTkButton(self.bottom_frame, text="Process Audio", command=self.start_processing)
        self.process_audio_btn.pack(side='left', padx=5)

        self.file_label = ctk.CTkLabel(self.bottom_frame, text="No file selected...", text_color="gray")
        self.file_label.pack(side='left', padx=10)
        
#-----------------------------------------------------------------------------------------------------------------------

    def translate(self):
        
        text = self.input_box.get("0.0","end").strip()

        if not text or text == self.placeholder:
            return
        
        target_language_name = self.lang_var.get()

        if target_language_name == "Select Language":
            return

        target_code = LANGUAGES[target_language_name]

        translated_text = GoogleTranslator(source='auto',target=target_code).translate(text)

        self.output_box.configure(state="normal")
        self.output_box.delete("0.0","end")
        self.output_box.insert("0.0",translated_text)
 
        self.output_box.configure(state="disabled")

#-----------------------------------------------------------------------------------------------------------------------

    def start_speaking(self):
        threading.Thread(target=self.listen_text, daemon=True).start()

    def update_text_box(self, box, text, disable=True):
        box.configure(state="normal")
        box.delete("0.0", "end")
        box.insert("0.0", text)
        if disable:
            box.configure(state="disabled")

#-----------------------------------------------------------------------------------------------------------------------

    def listen_text(self):

        text = self.output_box.get("0.0", "end").strip()

        if not text or text == "Translated Text appears here":
            return

        try:
            # Get selected language
            target_language_name = self.lang_var.get()
            target_code = LANGUAGES.get(target_language_name, "en")

            # Convert text → speech file
            tts = gTTS(text=text, lang=target_code, slow=False)
            filename = f"translated_audio_{int(time.time())}.mp3"
            tts.save(filename)

            # Play using pygame
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            # Wait until finished
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.stop()

            # Remove temp file
            if os.path.exists(filename):
                os.remove(filename)

        except Exception as e:
            print("Speech Error:", e)

#-----------------------------------------------------------------------------------------------------------------------
   
    def speak_text(self):
        recognizer = sr.Recognizer()

        try:
            with sr.Microphone(device_index=1) as source:
                print("Listening...")

                recognizer.adjust_for_ambient_noise(source, duration=1)

                audio = recognizer.listen(source,timeout=3,phrase_time_limit=5)

            print("Processing...")
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            self.input_box.delete("0.0", "end")
            self.input_box.insert("0.0", text)
            self.input_box.configure(text_color="white")

        except sr.WaitTimeoutError:
            print("You didn’t start speaking")

        except sr.UnknownValueError:
            print("Could not understand")

        except Exception as e:
            print("Error:", e)  

app = translator()
app.mainloop()        