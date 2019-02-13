from pygame import mixer
import time

mixer.init()


def play_audio(file):
    mixer.music.load(file)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)


def stop_audio():
    mixer.music.stop()


def pause_audio():
    mixer.music.pause()


def unpause_audio():
    mixer.music.unpause()
