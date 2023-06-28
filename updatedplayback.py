#necessary imports
import pyglet
#note that win32api is not imported or used in the main experiment file since its function is taken over by pygame there
from win32api import GetSystemMetrics
from datetime import datetime
from pyglet import clock as pyclock

# This will allow pyglet to find the FFmpeg binaries in the lib sub-folder located in your running script folder
pyglet.options['search_local_libs'] = True

# determine display size - note this is handled by a pygame command in the main experiment file
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# create a window to display the video
window = pyglet.window.Window(width, height)

# define path to the video
vidPath = "C:/Users/powel/Documents/Documents/Professional/Research/UO/NBP/Video/tedx.mpeg"

#define audio driver (directs pyglet to determine which is installed and use that)
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

# create a media player object
player = pyglet.media.Player()

# create a source object
source = pyglet.media.StreamingSource()

# load the media from the source
MediaLoad = pyglet.media.load(vidPath)
print(MediaLoad)

# add this media to the queue
player.queue(MediaLoad)

# play the video
player.play()

#define event to send trigger every second
def sectrigger(tick):
    now = datetime.now()
    curtime = now.strftime('%d-%m-%Y, %H:%M:%S.%f')
    print('sent sec trigger at ' + str(curtime))
    
# define draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # if player source exist
    # and video format exist
    if player.source and player.source.video_format:
        # get the texture of video and
        # make surface to display on the screen
        player.get_texture().blit(0, 0)

# define key press event
@window.event
def on_key_press(symbol, modifier):
    #define current time
    now = datetime.now()
    curtime = now.strftime('%d-%m-%Y, %H:%M:%S.%f')
    # pause/play if spacebar pressed
    if symbol == pyglet.window.key.SPACE:
        if player.playing == True:
            print("movie paused at " + curtime)
            player.pause()
        elif player.playing == False:
            print("restarting movie at " + curtime)
            player.play()

    # calibration start/stop if 'c' pressed
    if symbol == pyglet.window.key.C:
        if player.playing == True:
            player.pause()
            print("pausing and starting calibration at " + curtime)
        elif player.playing == False:
            print("restarting movie at " + curtime)
            player.play()
    
    #for testing only! - note you will have to reopen the OpenSesame window to continue the experiment
    #ends pyglet playback to save time during tests :)
    if symbol == pyglet.window.key.S:
        window.close()
        

#set full-screen mode
window.set_fullscreen(True)

#schedule the sending of a trigger every second
pyclock.schedule_interval(sectrigger,1)

# run the pyglet application
pyglet.app.run()
