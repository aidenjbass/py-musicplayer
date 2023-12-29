import os, random, threading
from audioplayer import AudioPlayer
from pynput import keyboard

player = None
controlsPause = '-'
controlsResume = '='

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    
    if 'char' in dir(key): 
        if key.char == controlsPause:
            player.pause()
        
        if key.char == controlsResume:
            player.resume()

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# assign directory
directory = '/Users/aiden/Library/CloudStorage/OneDrive-Personal/Music/80s/'
aWavFile = '/Users/aiden/Library/CloudStorage/OneDrive-Personal/Music/get-him-back-we-are-never-ever-getting-back-together-tv-mashup.wav'

def inOrder():
    # iterate over files in that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if its a file
        if os.path.isfile(f):
            # Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
            print(filename)
            AudioPlayer(f).play(block=True)

def shuffle():
    random_f = random.choice(os.listdir(directory))
    f = os.path.join(directory, random_f)
    # checking if its a file
    if os.path.isfile(f):
        # check if its an audio file
        if f.lower().endswith(('.mp3', '.wav')):
            # Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
            AudioPlayer(f).play(block=True)

def play():
    global player
    random_f = random.choice(os.listdir(directory))
    f = os.path.join(directory, random_f)
    # checking if its a file
    if os.path.isfile(f):
        # check if its an audio file
        if f.lower().endswith(('.mp3', '.wav')):
            player = AudioPlayer(f)
            try:
                player.play(block=True)
            except Exception as e:
                print('Error: ', e)

while True:
    thread_one = threading.Thread(target=play())
    thread_one.start()