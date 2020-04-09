from pygame import mixer
import random

_songs = ['song_0.mp3', 'song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3', 'song_5.mp3', 'song_6.mp3', 'song_7.mp3', 'song_8.mp3', 'song_9.mp3']

_currently_playing_song = None
_past_playing_song = None


def play_new_song():
    global _currently_playing_song, _past_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song or next_song == _past_playing_song:
        next_song = random.choice(_songs)
    _past_playing_song = _currently_playing_song
    _currently_playing_song = next_song
    mixer.music.load(next_song)
    mixer.music.play()


mixer.init()

print("Welcome to Sebastien's music player!!!")

while True:

    print("1. Press 'p' to play song")
    print("2. Press 'x' to skip song")
    print("3. Press 'q' to quit music player\n")

    answer = input("Enter a command: ")
    print("\n" * 2)
    if answer == "p" or answer == "x":
        play_new_song()
    elif answer == "q":
        mixer.music.stop()
        break


quit()
