from neurosity import NeurositySDK
from dotenv import load_dotenv
import os
import time
import csv
import random

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
split = 5

def callback(data):
    global timeStart  # Declare timeStart as a global variable
    global marker  # Declare marker as a global variable
    global split

    #print(".")
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

    for i in range(len(data["psd"])):
        data["psd"][i].append(marker)
        with open('demo.csv', mode='a') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow(data["psd"][i])

# unsubscribe = neurosity.brainwaves_raw(callback)
unsubscribe = neurosity.brainwaves_psd(callback)
time.sleep(20)
unsubscribe()