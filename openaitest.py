from gtts import gTTS
import pygame
from tempfile import TemporaryFile

def text_to_speech(text, lang='en'):
    # Initialize the gTTS object
    tts = gTTS(text=text, lang=lang)

    # Create a temporary file to save the speech as MP3
    with TemporaryFile() as tmp_file:
        # Save the speech as an MP3 file
        tts.write_to_fp(tmp_file)

        # Rewind the file to the beginning for playback
        tmp_file.seek(0)

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Load the MP3 file into Pygame mixer
        pygame.mixer.music.load(tmp_file)
        
        # Play the speech
        pygame.mixer.music.play()

        # Wait for the speech to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

if __name__ == "__main__":
    text = "My name is khan"
    text_to_speech(text)
