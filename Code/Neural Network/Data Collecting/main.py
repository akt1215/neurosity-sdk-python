from neurosity import NeurositySDK
from dotenv import load_dotenv
import os
import time
import csv
import random
import math
import threading
from playsound import playsound

load_dotenv()

neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID")
})

neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})

info = neurosity.get_info()
print(info)
timeStart = time.time()
marker = 0
split = 2

def callback(data):
    global timeStart  # Declare timeStart as a global variable
    global marker  # Declare marker as a global variable
    global split

    # print(".")
    # print(round((time.time() - timeStart) % split))
    # if round((time.time() - timeStart) % split) == 0:
    if (math.ceil(time.time() - timeStart) % split) == 0:
        # play sound B4.mp3
        sound_file_path = "/workspaces/neurosity-sdk-python/Code/Neural Network/Data Collecting/B4.mp3"
        playsound(sound_file_path)

        marker = 1 - marker
        if marker == 0:
            print("CLOSE")
        else:
            print("OPEN")
        split = random.randint(2, 3)
        # print(split)
        timeStart = time.time()
        time.sleep(0.1)

    # for i in range(len(data["psd"])):
    #     data["psd"][i].append(marker)
    #     with open('demo.csv', mode='a') as data_file:
    #         data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #         data_writer.writerow(data["psd"][i])

    for i in range(len(data["data"])):
        data["data"][i].append(marker)
        with open('demo3.csv', mode='a') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow(data["data"][i])

# unsubscribe = neurosity.brainwaves_raw(callback)
# unsubscribe = neurosity.brainwaves_psd(callback)
unsubscribe = neurosity.brainwaves_raw(callback)
time.sleep(30)
unsubscribe()