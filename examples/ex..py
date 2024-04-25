import serial
import time

# Open serial connection to Arduino
arduino = serial.Serial('COM3', 9600)  # Change 'COM3' to the appropriate port

# Wait for Arduino to reset
time.sleep(2)

# Send commands to Arduino
arduino.write(b'A')  # Send command 'A'
response = arduino.readline().decode().strip()
print("Response from Arduino:", response)

arduino.write(b'B')  # Send command 'B'
response = arduino.readline().decode().strip()
print("Response from Arduino:", response)

# Close serial connection
arduino.close()
