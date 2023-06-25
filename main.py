import os
import sys
import time
import vlc

def run(file_name):
    file_path = ""
    volume = 0

    if file_name[0] == '/' or file_name[0] == '.':
        file_path = file_name
    else:
        file_path = "{}/{}".format(os.getcwd(), file_name)

    instance = vlc.Instance('--fullscreen')

    player = instance.media_player_new()

    volume = player.audio_get_volume()
    
    media = instance.media_new(file_path)

    player.set_media(media)

    print("playing file       : {}".format(media.get_mrl()))
    print("playing with volume: {}".format(volume))

    player.play()

    time_start = time.time()

    while (time.time() - time_start < 15):
        time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) == 0 or len(file_name) > 0:
        sys.exit()

    file_name = sys.argv[1]

    run(file_name)
