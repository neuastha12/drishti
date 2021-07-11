# AVI UPADHYAY
import pyttsx3
import smtplib
import email
import email.encoders
import email.mime.text
import email.mime.base
import smtplib
import face_recognition
import speech_recognition as sr
import datetime
import winshell  # recyclebin
import os
import json  # weather
import feedparser
import ctypes
import shutil
from cv2 import cv2  # camera  #can be used for img, obj recognition
import random  # songs
import requests
from requests import get  # ip
import wikipedia
import webbrowser
import pywhatkit as kit  # whatsapp msg

import sys  # exit
import winsound  # pip
import pyautogui
import time
import urllib.request
import twilio
import pyjokes
import spacy
import wolframalpha  # to calculate strings into formula
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from projectGui import Ui_projectGui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # ZIRA x
engine.setProperty('rate', 200)


def take_picture():
    print("Scanning Face....")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('D:\\Documents\\Project\\Jarvis\\Picture.jpg', frame)
    cv2.destroyAllWindows()
    cap.release()
    print("Face scan complete.")


def analyze_user():
    print("Analyzing Face...")
    # Picture of Me as a baseline comparison
    baseimg = face_recognition.load_image_file(
        "D:\\Documents\\Project\\Jarvis\\Me.jpg")
    baseimg = cv2.cvtColor(baseimg, cv2.COLOR_BGR2RGB)

    myface = face_recognition.face_locations(baseimg)[0]
    encodemyface = face_recognition.face_encodings(baseimg)[0]
    cv2.rectangle(baseimg, (myface[3], myface[0]),
                  (myface[1], myface[2]), (255, 0, 255), 2)

    # cv2.imshow("Test", baseimg)
    # cv2.waitKey(0)

    # Sample image of face picture
    sampleimg = face_recognition.load_image_file(
        "D:\\Documents\\Project\\Jarvis\\Picture.jpg")
    sampleimg = cv2.cvtColor(sampleimg, cv2.COLOR_BGR2RGB)

    try:
        samplefacetest = face_recognition.face_locations(sampleimg)[0]
        encodesamplefacetest = face_recognition.face_encodings(sampleimg)[
            0]
    except IndexError as e:
        print("Index Error. Authentication Failed.")
        sys.exit()
    # cv2.rectangle(sampleimg, (samplefacetest[3], samplefacetest[0]), (samplefacetest[1], samplefacetest[2]),
    #            (255, 0, 255), 2)

    # cv2.imshow("Test", sampleimg)
    # cv2.waitKey(0)

    result = face_recognition.compare_faces(
        [encodemyface], encodesamplefacetest)
    resultstring = str(result)
    # print(resultstring)

    if resultstring == "[True]":
        print("User Authenticated. Welcome Back!")
        TaskExecution()
    else:
        print("Authentication Failed. Good Bye!")


take_picture()
analyze_user()


def speak(audio):  # TTS
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=667a3dfcfc234813a777634ef83386eb"
    main_page = requests.get(main_url).json()
    # print_mainpage
    articles = main_page["articles"]
    # print_articles
    head = []
    day = ["first", "second"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is:",head[i])
        speak(f"today's {day[i]}news is:{head[i]}")

#   def takecommand():
#       r = sr.Recognizer()
#       with sr.Microphone() as source:
#           print("Listening...")
#           r.pause_threshold = 1
#           audio = r.listen(source, timeout=5, phrase_time_limit=5)

#       try:
#          print("Recognizing...")
#           query = r.recognize_google(audio, language='en=in')
#           print(f"user said: {query}")

#       except Exception as e:
#           print(e)
#           speak("Say that again")
#           return "none"
#       return query


def pdf_reader():
    book = open('D:\\Documents\\Project\\Jarvis\\py3.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in a book{pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def wish():  # to wish
    hour = (datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour > 12 and hour < 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("I am Drishti, your personal desktop assistant. How may i help you?")


def awish():  # to wish
    hour = (datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        speak(f"Hey, good morning , its {tt}")
    elif hour > 11 and hour < 18:
        speak(f"Hey, good afternoon, its {tt}")
    else:
        speak(f"Hey, good evening, its {tt}")
    speak(" What can i do for you miss?")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("drishti016345@gmail.com", "drishti345")
    server.sendmail("drishti016345@gmail.com", to, content)
    server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en=in')
            print(f"user said: {query}")

        except Exception as e:
            print(e)
            speak("Say that again")
            return "none"
        return query

    def TaskExecution(self):
        wish()
        while True:
            if 1:

                self.query = self.takecommand()

                # logic building for tasks

                if "open notepad" in self.query:
                    npath = "C:\\Windows\\System32\\notepad.exe"
                    os.startfile(npath)

                elif "close notepad" in self.query:
                    speak("okay sure, Closing notepad")
                    os.system("taskkill /f /im notepad.exe")

                elif 'open command prompt' in self.query:
                    os.system("start cmd")

                elif 'open gmail' in self.query:
                    webbrowser.open_new_tab("https://www.gmail.com")
                    speak("Gmail is open")
                    time.sleep(5)

                elif "shut down" in self.query:
                    speak("Ok , your system will shut down in 10 seconds")
                    os.system("shutdown /s /t 5")

                elif "restart" in self.query:
                    speak("Ok , your system will restart in 10 seconds")
                    os.system("shutdown /r /t 5")

                elif "sleep the system" in self.query:
                    speak("Ok , your system is sleeping")
                    os.system("rund1132.exe powrprof.dll,SetSupendState 0,1,0")

                elif "switch the window" in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif "news" in self.query:
                    speak("Please wait for a while, fetching the latest news")
                    news()
                    time.sleep(5)

                elif "hi" in self.query or "hey" in self.query:
                    speak("hello, may i help you with something")

                elif "sleep" in self.query:
                    speak("okay thankyou, i am going to sleep you can call me anytime")
                    break

                elif "open camera" in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif "play music" in self.query:  # MUSIC
                    music_dir = "C:\\Users\\Dell\\Music"
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    for song in songs:
                        if song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, songs[0]))
                            time.sleep(5)

                elif "internet speed" in self.query:

                    import speedtest
                    st = speedtest.Speedtest()
                    d1 = st.download()
                    up = st.upload
                    speak(
                        f"We have {d1} bit per second downloading speed and {up} bit per second uploading speed")

                    try:
                        os.system('cmd /k "speedtest"')

                    except:
                        speak("There is no internet connection")

                elif "tell me a joke" in self.query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                    time.sleep(5)

                elif "ip address" in self.query:
                    ip = get('https://api.ipify.org').text6
                    speak(f"Your IP address is {ip}")
                    time.sleep(5)

                elif "calculate" in self.query:
                    speak('I can answer your computational and geographical questions')
                    app_id = "R9U86W-RJHAJP7KJ7"
                    client = wolframalpha.Client(app_id)
                    indx = self.query.lower().split().index('calculate')
                    self.query = self.query.split()[indx + 1:]
                    res = client.self.query(' '.join(self.query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    speak("The answer is " + answer)
                    time.sleep(5)

                elif "weather" in self.query:

                    # Google Open weather website
                    # to get API of Open weather
                    api_key = "2c0944d3eamshbb808a41f268fc7p1eb358j"
                    base_url = "http://api.openweathermap.org/data/2.5/weather?"
                    speak(" City name ")
                    print("City name : ")
                    city_name = takecommand()
                    complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                    response = requests.get(complete_url)
                    x = response.json()

                    if x["cod"] != "404":
                        y = x["main"]
                        current_temperature = y["temp"]
                        current_pressure = y["pressure"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        print(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(
                            current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

                    else:
                        speak("Sorry, City Not Found ")

                elif "wikipedia" in self.query:
                    speak("Searching Wikipedia...")
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=3)
                    speak("According to wikipedia")
                    speak(results)
                    print(results)
                    time.sleep(5)

                elif "youtube" in self.query:
                    webbrowser.open("youtube.com")
                    time.sleep(5)

                elif "facebook" in self.query:
                    webbrowser.open("facebook.com")
                    time.sleep(5)

                elif "google" in self.query:
                    speak("What should i search on google?")
                    cm = takecommand().lower()
                    webbrowser.open(f"{cm}")
                    time.sleep(5)

                elif "twitter" in self.query:
                    webbrowser.open("twitter.com")
                    time.sleep(5)

                elif "instagram" in self.query:
                    webbrowser.open("instagram.com")
                    time.sleep(5)

                elif 'open youtube' in statement:
                    webbrowser.open_new_tab("https://www.youtube.com")
                    speak("youtube is open now")
                    time.sleep(5)

                elif "pokhara university" in self.query:
                    webbrowser.open("pu.edu.np")

                elif "nepal engineering" in self.query:
                    webbrowser.open("nec.edu.np")

                elif 'open our presentation' in self.query:
                    speak("opening my Power Point presentation")
                    power = r"D:\\Documents\\Project\\academic_writing_skills.ppt"
                    os.startfile(power)

                elif 'empty recycle bin' in self.query:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    speak("Recycle Bin Recycled")

                elif "don't listen" in self.query or "stop listening" in self.query:
                    speak(
                        "for how much time you want to stop me from listening commands")
                    a = int(takecommand())
                    time.sleep(a)
                    print(a)

                elif "where is" in self.query:
                    self.query = self.query.replace("where is", "")
                    location = self.query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open(
                        "https://www.google.com/maps/place/" + location + "")

                elif 'exit' in self.query or 'bye' in self.query or 'quit' in self.query or 'stop' in query:
                    speak("Good bye, Have a nice day!")
                    exit(0)

                elif 'alarm' in self.query:
                    # set alarm to ...
                    speak("please tell me the time to set alarm")
                    tt = takecommand()
                    tt = tt.replace("set alarm to ", "")  # 05:30 a.m.
                    tt = tt.replace(".", "")
                    tt = tt.upper()
                    import MyAlarm
                    MyAlarm.alarm(tt)

                    # VOLUME_CONTROL
                elif 'volume up' in self.query:
                    pyautogui.press("volumeup")

                elif 'volume dowm' in self.query:
                    pyautogui.press("volumedown")

                elif 'mute' in self.query:
                    pyautogui.press("volumemute")

                elif "open word" in self.query:
                    speak("Opening Microsoft Word")
                    os.startfile(
                        'C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.exe')
                elif "open excel" in self.query:
                    speak("Opening Microsoft Excel")
                    os.startfile(
                        'C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.exe')
                elif "open powerpoint" in self.query:
                    speak("Opening Microsoft Powerpoint")
                    os.startfile(
                        'C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.exe')

                elif "read pdf" in self.query:
                    pdf_reader()

                elif "cpu power" in self.query or "battery" in self.query:
                    import psutil
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"our system have {percentage} percent battery")
                    if percentage >= 75:
                        speak("we have enough power to continue our work")
                    elif percentage >= 40 and percentage < 75:
                        speak(
                            "we should connect our syatem to charging point to charge our battery")
                    elif percentage >= 15 and percentage < 30:
                        speak(
                            "we don't have enough power to work, please connect to charging")
                    elif percentage < 15:
                        speak(
                            "we have very low power, please connect to charging the system will shutdown very soon")

                elif "cpu temperature" in self.query:
                    import wmi
                    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
                    temperature_infos = w.Sensor()
                    for sensor in temperature_infos:
                        if sensor.SensorType == u'Temperature':
                            print(sensor.Name)
                            # speak(sensor.Name)
                            print(sensor.Value)
                            # speak(sensor.Value)

                elif "will you be my girlfriend" in self.query:
                    speak("I'm not sure about it, may be you should give me some time")

                elif "i love you" in self.query:
                    speak("I find it hard to understand")

                elif "write a note" in query:
                    speak("What should i write, miss")
                    note = takecommand()
                    file = open('jarvis.txt', 'w')
                    speak("Should i include date and time")
                    snfm = takecommand()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("%I:%M %p")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)

                elif "show note" in query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r")
                    print(file.read())
                    speak(file.read(6))
                    time.sleep(5)

                elif "mobile camera" in query:
                    import numpy as np
                    URL = "http://192.168.1.69:8080/shot.jpg"
                    while True:
                        img_arr = np.array(
                            bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                        img = cv2.imdecode(img_arr, -1)
                        cv2.imshow('IPWebcam', img)
                        q = cv2.waitKey(1)
                        if q == ord('q'):
                            break

                    cv2.destroyAllWindows()

                elif "send whatsapp message" in query:
                    kit.sendwhatmsg("+9779811694999", "This is testing", 1, 20)
                    time.sleep(5)

                elif "send phone message" in query:
                    speak("What should i say?")
                    msg = takecommand()

                    from twilio.rest import Client

                    # Your Account Sid and Auth Token from twilio.com/console
                    # and set the environment variables. See http://twil.io/secure
                    account_sid = 'ACca4e327ef871c88bb10894b1d33d14c6'
                    auth_token = '0ff47376d36a0e6104b837c8a14c377e'
                    client = Client(account_sid, auth_token)

                    message = client.messages.create(
                        body=msg,
                        to='+9779813221626',
                        from_='+17865047736'
                    )

                    print(message.sid)
                    speak("The message is sent!")
                    time.sleep(5)

                elif "make a call" in query:
                    from twilio.rest import Client
                    account_sid = 'ACca4e327ef871c88bb10894b1d33d14c6'
                    auth_token = '0ff47376d36a0e6104b837c8a14c377e'
                    client = Client(account_sid, auth_token)

                    message = client.calls.create(
                        twiml='<Response><Say>This is Drishti speaking. Have a good day, everyone</Say></Response>',
                        from_='+17865047736',
                        to='+9779813221626'

                    )

                    print(message.sid)
                    speak("The call is sent!")
                    time.sleep(5)

                elif 'send a mail' in query:
                    try:
                        speak("What should I say?")
                        content = takecommand()
                        speak("whom should i send the email?")
                        to = input()
                        sendEmail(to, content)
                        speak("Email has been sent !")
                    except Exception as e:
                        print(e)
                        speak("I was not able to send the email")

                elif "open adobe reader" in self.query:
                    apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"

    if __name__ == '__main__':
        while True:
            permission = takecommand(self)
            if "wake up" in permission:
                TaskExecution()
            elif "goodbye" in permission or "exit" in permission or "quit" in permission:
                speak("it was nice talking to you. Take care")
                sys.exit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_projectGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(
            "D:\\Documents\\Project\\wallpaper\\Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "D:\\Documents\\Project\\wallpaper\\loading.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "D:\\Documents\\Project\\wallpaper\\looping.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(QT.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
drishti = Main()
drishti.show()
exit(app.exec_())
