import speech_recognition as sr
import pyttsx3


class Friday():
    def __init__(self) -> None:
        self.mendengarkan = sr.Recognizer()
        self.engine = pyttsx3.init("sapi5")
        # kecepatan baca
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', 125)
        # jenis suara [0] male [1] female
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def take_command(self):
        with sr.Microphone() as source:
            print("mendengarkan")
            voice = self.mendengarkan.listen(source)
            command = self.mendengarkan.recognize_google(voice)
            command = command.lower()
            return command
