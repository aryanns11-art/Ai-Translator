import customtkinter as ctk
from PIL import Image, ImageDraw
from deep_translator import GoogleTranslator


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

    def framess(self):

        top_label = ctk.CTkLabel(self,text="Translator App")
        top_label.pack(anchor='nw',pady=5)
    
        #---------------------------Button Frame--------------------------------------------------------

        self.button_frame = ctk.CTkFrame(self,height=70,fg_color="#ceebfd")
        self.button_frame.pack(fill='x',pady=2)
        self.button_frame.pack_propagate(False)

        self.trans_btn = ctk.CTkButton(self.button_frame,text="Translate",command=self.translate)
        self.trans_btn.pack(side='left',padx=5,pady=5)

        self.lang_var = ctk.StringVar(value="Select Language")
        self.lang_dropdown = ctk.CTkOptionMenu(self.button_frame,values=['Select Language']+list(LANGUAGES.keys()),variable = self.lang_var, width=150)
        self.lang_dropdown.pack(side='right',padx=5,pady=5)

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
        self.input_box_label = ctk.CTkLabel(self.left_frame,text="Enter text: ")
        self.input_box_label.pack(anchor='nw',pady=2)



        self.input_box = ctk.CTkTextbox(self.left_frame,height=180)
        self.input_box.pack(fill="both",expand=True,padx=5,pady=5)
        self.input_box.insert("0.0", "Enter text to translate..")

        self.output_box_label = ctk.CTkLabel(self.right_frame, text="Translated Text:")
        self.output_box_label.pack(anchor='nw',pady=2)
        
        self.output_box = ctk.CTkTextbox(self.right_frame, height=180)
        self.output_box.pack(fill="both", expand=True, padx=5, pady=5)

        self.output_box.insert("0.0", "Translated Text appears here..")
        self.output_box.configure(state="disabled")

    def translate(self):
        
        text = self.input_box.get("0.0","end")

        if not text:
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
        
        
app = translator()
app.mainloop()        