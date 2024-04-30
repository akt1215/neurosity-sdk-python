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
    with open('raw_data.txt', 'a') as file:
        file.write(str(data) + '\n')
    
    # for i in range(len(data["data"])):
    #     with open('grab2.csv', mode='a') as data_file:
    #         data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #         data_writer.writerow(data["data"][i])

    for i in range(len(data["psd"])):
        with open('psd.csv', mode='a') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow(data["psd"][i])


# unsubscribe = neurosity.brainwaves_raw(callback)
unsubscribe = neurosity.brainwaves_psd(callback)
time.sleep(10)
unsubscribe()