"""import time
import csv
import random 

data = [1,2,3,4,5]
timeStart = time.time() # Declare timeStart as a global variable
marker = 0 # Declare marker as a global variable
split = 5

for _ in range(40):
    print(round((time.time() - timeStart) % split))
    if round((time.time() - timeStart) % split) == 0:
        time.sleep(0.5)
        marker = 1 - marker
        if marker == 0:
            print("close")
        else:
            print("open")
        split = random.randint(3, 6)
        print(split)
        timeStart = time.time()
        
    for i in range(len(data)):
        data = [1,2,3,4,5]
        data.append(marker)
        with open('demo2.csv', mode='a') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow(data)
    time.sleep(0.5)"""

from pydub import AudioSegment
from pydub.playback import play

def play_audio(file):
    sound = AudioSegment.from_mp3(file)
    play(sound)

# Replace 'your_music.mp3' with the path to your MP3 file
play_audio('/workspaces/neurosity-sdk-python/Code/Neural_Network/Data_Collecting/B4.mp3')