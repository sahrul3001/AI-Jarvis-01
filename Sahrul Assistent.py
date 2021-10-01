from friday import Friday
import pywhatkit
import datetime
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time as t

AI = "Friday"
MASTER = "sahrul"


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        Friday().talk("Hello Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        Friday().talk("Hello Good Afternoon" + MASTER)
    else:
        Friday().talk("Hello Good Evening" + MASTER)
    Friday().talk(f"I'm {AI} what do you want")


def run_friday():
    try:
        command = Friday().take_command()
        if 'play' in command:
            song = command.replace("play", "")
            Friday().talk("playing" + song)
            print("playing" + song)
            pywhatkit.playonyt(song)
        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            Friday().talk("time now is " + time)
        elif "wikipedia" in command:
            src = command.replace("wikipedia", "")
            info = wikipedia.summary(src, sentences=1)
            Friday().talk("searching wikipedia")
            print(info)
            Friday().talk(info)
        elif "login" in command:
            Friday().talk("Login Elearning")
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
                Friday().talk(f"The result of sigma is{hasil}")
            print("=== Rumus Notasi Sigma ===")
            Friday().talk("calculate sigma, please enter a number")
            bb = int(input("Masukan Batas Bawah : "))
            ba = int(input("Masukan Batas Atas : "))
            sigma(bb, ba)
        elif "say hello" in command:
            Friday().talk("Hello Para Peserta Kelas, Reguler, Bagaimana Kabar kalian")
            print("Hello Para Peserta Kelas Reguler")
        elif "stop" in command:
            Friday().talk(f"Okey, run me again if you need help {MASTER}")
            print("exit Program")
            sys.exit()
        else:
            Friday().talk("not any intruction")
            print(command)
    except:
        Friday().talk(f"Call me {AI} frist")


wishMe()
