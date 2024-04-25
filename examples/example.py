from neurosity import NeurositySDK
from dotenv import load_dotenv
import os
import time
import csv

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

def callback(data):
    print(data)
    for i in range(len(data["data"])):
        with open('data.csv', mode='a') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow(data["data"][i])

unsubscribe = neurosity.brainwaves_raw(callback)
time.sleep(2)
neurosity.add_marker("eyes-closed")
time.sleep(2)
unsubscribe()