# Part 1: Working with Dates (today.txt)

# 13.1: Write today's date to a file as a string
# 13.2: Read the file into a string
# 13.3: Parse the string back into a date object

from datetime import date, datetime

print("===== Dates Section =====\n")

# 13.1 Write today's date
today = date.today()
print("Today's date (date object):", today)

with open("today.txt", "w") as file:
    file.write(today.isoformat())

print("Date written to today.txt\n")

# 13.2 Read from file
with open("today.txt", "r") as file:
    today_string = file.read()

print("Read from file (string):", today_string)

# 13.3 Parse the string
parsed_date = datetime.strptime(today_string, "%Y-%m-%d").date()
print("Parsed date object:", parsed_date)


# Part 2: Multiprocessing

# Create 3 processes that:
# - Wait random time between 0 and 1 second
# - Print current time
# - Exit

import multiprocessing
import time
import random

print("\n===== Multiprocessing Section =====\n")

def worker():
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    
    print(f"{multiprocessing.current_process().name} waited {wait_time:.3f} seconds")
    print(f"Current time: {datetime.now()}\n")

if __name__ == "__main__":
    processes = []

    print("Starting processes...\n")

    # Create and start 3 processes
    for i in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All processes finished.")