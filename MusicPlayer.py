# by steel99xl
from Tkinter import *
import pygame as pg
import easygui
app = Tk()
app.title("Music Player to be ported to easygui")
app.geometry("200x200")

music_file=''

print("Only works with mp3 files because what ells do people save music as?")
global f
global v
v = 0.8


pg.init()

def select():
    global music_file
    music_file = easygui.fileopenbox(filetypes = ['*.mp3'])
    play_music(music_file, volume=v)

def play_music(music_file, volume=v):
    global v
    pg.init()

    # mixer config
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 211680    # number of samples (might need with diffrent types of music)
    pg.mixer.init(freq, bitsize, channels, buffer)
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} did not catch fire".format(music_file))
    except pg.error:
        print("This has to be here other wise i get a syntax error")
        return
    pg.mixer.music.play()
  # optional volume 0 to 1.0
    volume = v

def play():
    print("{} is probaly making noise.".format(music_file))
    pg.init()
    pg.mixer.music.unpause()

def pause():
    print("{} has now been paused.".format(music_file))
    pg.init()
    pg.mixer.music.pause()

def stop():
    print("The song {} has been MURDER KILLED!!!! and reserected".format(music_file))
    pg.mixer.music.pause()
    play_music(music_file, volume=v)

def down():
    print("Down")
    global v
    v -= 0.1
    pg.init()
    pg.mixer.music.unpause()

    print v

def up():
    print("Up")
    global v
    v += .1
    pg.init()
    pg.mixer.music.unpause()

    print v


btnOpen = Button(app)
btnOpen.grid(row=10, column=0)
btnOpen.configure(text = "Open", command = select)

btnPlay = Button(app, text = "Play", command = play)
btnPlay.grid()

btnPause = Button(app)
btnPause.grid()
btnPause.configure(text = "Pause", command = pause)

btnKill = Button(app)
btnKill.grid()
btnKill.configure(text = "Restart", command = stop)

btnUp = Button(app)
btnUp.grid()
btnUp.configure(text = "up", command = up)

btnDown = Button(app)
btnDown.grid()
btnDown.configure(text = "Down", command = down)

app.mainloop()
