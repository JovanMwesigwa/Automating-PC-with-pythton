import pyttsx3
import datetime
from selenium import webdriver

DRIVER_PATH = r'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


engine = pyttsx3.init()
voices = engine.getProperty('voices')

now = datetime.datetime.now()
current_time = datetime.time(now.hour, now.minute)



def tellTime():
    engine.runAndWait()
    engine.say('The time is {}'.format(current_time))

# getting the voice id voice
female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Changing to female voice
female_voice = engine.setProperty('voice', female_voice_id)
slow_down_speed_rate = engine.getProperty('rate')
engine.setProperty('rate', slow_down_speed_rate-60)

driver.get("http://www.python.org")

def Ruth():
    engine.say('Hi Jovan, This is Ruth, What can i do for you today?')

    engine.runAndWait()

    ask_for_time = input('Ask Ruth :')

    if 'time'.lower() in ask_for_time:
        tellTime()

Ruth()
engine.runAndWait()