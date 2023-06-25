import os
import sys
import time
import vlc

def play_file(file_path, length = 0):
    instance = vlc.Instance('--fullscreen')
    player = instance.media_player_new()
    media = instance.media_new(file_path)

    player.set_media(media)

    try:
        player.play()
        time.sleep(2)

        if length == 0:
            length = player.get_length() / 1000

        time_start = time.time()

        while (time.time() - time_start < length - 5):
            time.time()
            time.sleep(2)

        player.stop()
    except KeyboardInterrupt:
        if player.is_playing():
            player.stop()
        sys.exit()

def play_tabla(dir_dict):
    for dir, contents in dir_dict.items():
        for file in contents:
            play_file(file)

def organize_playback(dir_dict, dir_path):
    if not os.path.isdir(dir_path):
        sys.exit()

    dir_dict[dir_path] = ["{}/{}".format(dir_path, file) for
                          file in os.listdir(dir_path) if file.endswith('.mkv')]

    for file in os.listdir(dir_path):
        new_dir = "{}/{}".format(dir_path, file)
        if os.path.isdir(new_dir):
            organize_playback(dir_dict, new_dir)

if __name__ == "__main__":
    if len(sys.argv) == 0 or len(sys.argv[1]) == 0:
        sys.exit()

    dir_path = sys.argv[1]
    dir_dict = dict()

    organize_playback(dir_dict, dir_path)
    play_tabla(dir_dict)
