import time
from datetime import datetime
import pygame
import os
import random

new_year_time = datetime(2025, 1, 1, 0, 0, 0)

pygame.mixer.init()

tracks_folder = "./tracks/"

tracks = [f for f in os.listdir(tracks_folder) if f.endswith('.wav') or f.endswith('.mp3')]

new_year_music_file = "./new_year_file.wav"
pygame.mixer.music.set_volume(0.2)

def play_random_track():
    random_track = random.choice(tracks)
    track_path = os.path.join(tracks_folder, random_track)
    pygame.mixer.music.load(track_path)
    pygame.mixer.music.play()

while datetime.now() < new_year_time:
    play_random_track()
    print("Playing random track...")
    
    while pygame.mixer.music.get_busy():
        time.sleep(1)

pygame.mixer.music.set_volume(1)
print("Happy New Year!")
pygame.mixer.music.load(new_year_music_file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)
