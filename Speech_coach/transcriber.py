import speech_recognition as sr
from datetime import datetime

# Format the time as "h:m:s"
def clock():
    current_datetime = datetime.now()
    return f"{current_datetime.month}_{current_datetime.day}_{current_datetime.year}::{current_datetime.hour:02}_{current_datetime.minute:02}_{current_datetime.second:02}"

def record_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=15)

    print("Recording complete.")
    return audio

def transcribe_audio(audio):
    recognizer = sr.Recognizer()

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        print("Transcription: ", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def save_to_file(text, filename=None):
    if filename is None:
        filename = f"{clock()}transcript.txt"
    with open(filename, "w") as file:
        file.write(text)
    print(f"Transcription saved to {filename}")

if __name__ == "__main__":
    audio_data = record_audio()
    transcribed_text = transcribe_audio(audio_data)

    if transcribed_text:
        save_to_file(transcribed_text)
