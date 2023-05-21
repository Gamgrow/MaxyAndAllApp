import speech_recognition as sr
def commandd():
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
        print(text)