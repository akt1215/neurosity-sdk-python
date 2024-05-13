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

from playsound import playsound

# Replace 'sound_file_path' with the path to your sound file
sound_file_path = "/workspaces/neurosity-sdk-python/Code/Neural Network/Data Collecting/B4.mp3"

# Play the sound
playsound(sound_file_path)