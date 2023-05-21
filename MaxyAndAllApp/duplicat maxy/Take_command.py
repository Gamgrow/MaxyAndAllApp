
import speech_recognition as sr

class Takecommand():

    def command():
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print('listening...')

            r.pause_threshold = 5
            audio = r.listen(mic, timeout=45)

        try:
            print('recognizing...')
            text = r.recognize_google(audio)
            text = text.lower()
        except Exception as e:
            print(e)
            return text
        return text
    
    
