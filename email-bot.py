import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():  #use this function for english
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))

def get_info_in_hindi(): #use this function for hindi
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice, language='hi-IN')
            print(info)
            return info.lower()          
    except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))



def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give third party app access in your Google account
    server.login('Sender_Email', 'Sender_Email_Password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

#example email list
email_list = {
    'person1': 'person1@gmaail.com',
    'person2': 'person2@gmaail.com',
    'person3': 'person3@gmaail.com',
    'person4': 'person4@gmaail.com',
    'person5': 'person5@gmaail.com',
}


def email_bot():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    while(True):  
        talk('is the above message correct')
        hana = get_info()
        if 'yes' in hana:
            break
        else:
            talk('Please repeat the massage')
            message=get_info()
    send_email(receiver, subject, message)
    talk('Ok. Your email is sent. Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        email_bot()


email_bot()