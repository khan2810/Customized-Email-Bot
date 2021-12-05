# Customized-Email-Bot
* This is a customized repetitive email-bot for sending emails through voice commands created using python.
* I have created this bot using python and some of its useful libraries.
* With this bot, you can send unlimited emails to unlimited people without touching your computer. 
## Libraries used
* I have used the smtplib, SpeechRecognition, pyttsx3 and pyAudio libraries to implement this.
* [**_`smtplib`_**](https://docs.python.org/3/library/smtplib.html)  This is a preinstalled library in python for sending emails through your gmail.
* [**_`SpeechRecognition`_**](https://pypi.org/project/SpeechRecognition/)  This module is used for speech recognition through various engines and API's. We can recognise various languages using their corresponding codes in language attribute of `recognize_*()` method.
* [**_`pyttsx3`_**](https://pypi.org/project/pyttsx3/)  This is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
* [**_`pyAudio`_**](https://pypi.org/project/PyAudio/)  Here we have used `Microphone()` object for detecting audio. That is why we have to use PyAudio for supporting `Microphone()`object.
## How to Use
* for using it, you just need a cloth of single colour like blue, white, red, yellow, green etc.
* To use a particular color cloth, you just need to uncomment the lower and upper bounds for [HSV colour space](https://stackoverflow.com/questions/36817133/identifying-the-range-of-a-color-in-hsv-using-opencv/51686953) value of that color.
* I have used blue color cloth, if you want to try with some other color you can just uncomment that color's HSV bounds and commenting every other color.
* Make sure that your background doesn't contain the color of the cloth you are going to use.
* Run the program and come in front of webcam after 1 or 2 seconds, because it has to store the initial background frame.
* And now you can use your cloak to become invisible in good lighting conditions.
* Be careful in case of black color cloak, because your hairs may be black and your surrounding may have black parts too.
* you can even use multiple color cloth, in that case you have to uncomment the HSV ranges of all the colors the cloth contains because we have to process the current frame for all those colors.
