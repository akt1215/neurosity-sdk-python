import time

for i in range (10):
    print("hello")
    time.sleep(0.1)  # Optional: Adjust the delay if needed
    for _ in range(10):  # Print "hello" 10 times, effectively creating a delay
        time.sleep(0.2)
        print("hello", end=" ")
    print("\nworld")
