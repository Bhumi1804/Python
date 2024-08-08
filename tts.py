# import pyttsx3

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")

# engine.setProperty("voices",voices[0].id)

# def speak(query):
# 	engine.say(query)
# 	engine.runAndWait()

# if __name__ == "__main__":
# 	speak('thanks for watching')

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init("sapi5")

# Get available voices
voices = engine.getProperty("voices")

# Set the voice to the first voice in the list
engine.setProperty("voice", voices[0].id)

def speak(query):
    # Convert text to speech
    engine.say(query)
    engine.runAndWait()

if __name__ == "__main__":
    # Get text input from the user
    text_to_speak = input("Enter the text you want to convert to speech: ")
    speak(text_to_speak)

