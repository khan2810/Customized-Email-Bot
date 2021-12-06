# Customized-Email-Bot
* This is a customized repetitive email-bot for sending emails through voice commands created using python.
* I have created this bot using python and some of its useful libraries.
* With this bot, you can send unlimited emails to unlimited people without touching your computer. 
## Libraries used
* I have used the smtplib, SpeechRecognition, pyttsx3 and pyAudio libraries to implement this.
* [**_`smtplib`_**](https://docs.python.org/3/library/smtplib.html)  This is a preinstalled library in python for sending emails through your gmail.
* [**_`SpeechRecognition`_**](https://pypi.org/project/SpeechRecognition/)  This module is used for speech recognition through various engines and API's. We can recognise various languages using their corresponding codes in language attribute of `recognize_*()` method.
* [**_`pyttsx3`_**](https://pypi.org/project/pyttsx3/)  This is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
* [**_`pyAudio`_**](https://pypi.org/project/PyAudio/)  Here we have used ***Microphone()*** object for detecting audio. That is why we have to use PyAudio for supporting ***Microphone()*** object.
## How to Use
* for using it, you just need to install above libraries in your system.
* And then copy the code in your system and make the following changes.
* Firstly you have to put your email and password in place of 'Sender_Email' and 'Sender_Email_Password' respectively in the *send_email()* function.
* After that you need to change the *email_list* with with the ones to whom you want to send the emails.
* You can even send the mail in hindi, for this you just need to change the *get_info()* with the function *get_email_in_hindi()*.
* You can even use any language, you just need to pass the language code in the value of language attribute of *recognize_google()* method.
## Working Demo
