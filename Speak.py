import pyttsx3

def say(Text) :

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',160)
    print("  ")
    print(f"P.E.P.P.E.R. : {Text}")
    engine.say(text = Text)
    engine.runAndWait()
    print("  ")
    #print(voices[0].id)

say("Boss, at your service.")
