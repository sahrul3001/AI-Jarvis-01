import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time as t

AI = "Friday"
print(AI)
MASTER = "sahrul"
mendengarkan = sr.Recognizer()
engine = pyttsx3.init("sapi5")
# kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
# jenis suara [0] male [1] female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        talk("Hello Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        talk("Hello Good Afternoon" + MASTER)
    else:
        talk("Haello Good Evening" + MASTER)


def take_command():
    try:
        with sr.Microphone() as source:
            print("mendengarkan")
            voice = mendengarkan.listen(source)
            command = mendengarkan.recognize_google(voice)
            command = command.lower()
            if "friday" in command:
                print(command)
                command = command.replace("friday", "")
                talk(command)
                return command
            else:
                command = False
    except:
        print("no command")


def run_jarvis():
    try:
        command = take_command()
        if 'play' in command:
            song = command.replace("play", "")
            talk("playing" + song)
            print("playing" + song)
            pywhatkit.playonyt(song)
        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            talk("time now is " + time)
        elif "wikipedia" in command:
            src = command.replace("wikipedia", "")
            info = wikipedia.summary(src, sentences=1)
            talk("searching wikipedia")
            print(info)
            talk(info)
        elif "login" in command:
            talk("Login Elearning")
            browser = webdriver.Chrome('webdriver/chromedriver.exe')
            link = open("elearning/link.txt")
            el = link.readlines()
            url = el[0]
            browser.get(url)
            file = open("elearning/akun.txt")
            filebaca = file.readlines()
            username = filebaca[0]
            password = filebaca[1]
            login_username = browser.find_element_by_id("username")
            login_username.send_keys(username)
            login_password = browser.find_element_by_id("password")
            login_password.send_keys(password)
            login_password.send_keys(Keys.ENTER)
            t.sleep(1)
            jadwal = el[1]
            browser.get(jadwal)
        elif "sigma" in command:
            def sigma(bb, ba):
                k = int(input("Konstanta Pertama : "))
                k1 = int(input("Konstanta selanjutnya: "))
                listh = []
                for i in range(bb, ba):
                    k = k
                    k1 = k1
                    c = i * k + k1
                    listh.append(c)
                k *= ba
                k += k1
                listh.append(k)
                print(listh)
                hasil = sum(listh)
                print("Hasil Nilai Sigma =", hasil)
                talk(f"The result of sigma is{hasil}")
            print("=== Rumus Notasi Sigma ===")
            talk("calculate sigma, please enter a number")
            bb = int(input("Masukan Batas Bawah : "))
            ba = int(input("Masukan Batas Atas : "))
            sigma(bb, ba)
        elif "say hello" in command:
            talk("Hello Para Peserta Kelas, Reguler, Bagaimana Kabar kalian")
            print("Hello Para Peserta Kelas Reguler")
        elif "stop" in command:
            talk(f"Okey, run me again if you need help {MASTER}")
            print("exit Program")
            sys.exit()
        else:
            talk("not any intruction")
            print(command)
    except:
        talk(f"Call me {AI} frist")


wishMe()

while True:
    MASTER = "sahrul"
    mendengarkan = sr.Recognizer()
    engine = pyttsx3.init("sapi5")
    # kecepatan baca
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    # jenis suara [0] male [1] female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    talk(f"I am {AI} what do you want")
    run_jarvis()
    input()
