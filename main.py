import os
import eyed3

count =0
allcount=0

def update_album_info(directory):
    global count, allcount
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mp3', '.flac', '.ogg')):
                try :
                    file_path = os.path.join(root, file)
                    audiofile = eyed3.load(file_path)

                    if audiofile is None : raise Exception("failed reading file")
                    song_name = os.path.splitext(file)[0]
                    audiofile.tag.album = song_name
                    audiofile.tag.album_artist = song_name
                    audiofile.tag.save()
                    count+=1
                except Exception as e :
                    print(f"failed converting {os.path.splitext(file)[0]} , {e}")
                allcount+=1

if __name__ == "__main__":
    directory = "/storage/emulated/0/Music/"
    update_album_info(directory)
    print(f"successfully edited {count}/{allcount}")
