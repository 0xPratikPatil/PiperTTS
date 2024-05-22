import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Define the path to the folder containing audio files
folder_path = 'Jarvis/wav'

# Get a list of all files in the folder
audio_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Filter out only the audio files (assuming .mp3 and .wav formats, you can add more)
audio_files = [f for f in audio_files if f.endswith('.mp3') or f.endswith('.wav')]

# Function to play an audio file
def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Wait until the music finishes playing

# Iterate over each audio file and play it
for audio_file in audio_files:
    full_path = os.path.join(folder_path, audio_file)
    print(f"Playing {full_path}")
    play_audio(full_path)

# Quit the mixer
pygame.mixer.quit()
