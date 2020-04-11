
from pygame import *
from pygame import mixer ## here we import library pygame to bring mixer
mixer.init() ## Start the mixer

mixer.music.load("horse.mp3") # Load the song
mixer.music.set_volume(0.7) ## Set the Volume
mixer.music.play() # Play the mixer

while True:
    print("Press 'p' to pause and 'r' to resume")
    print("Press 'e' to exit the program")
    query = input(">>> ")

    if query == 'p':
        mixer.music.pause() # Pause Music
        print('Music is Pause >>> ')
    elif query == 'r':
        mixer.music.unpause() # Resume music
        print('resume Music .. ')
    elif query == 'e':
        mixer.music.stop() # Stop the Music
        print('Music is stopped :::')
        break