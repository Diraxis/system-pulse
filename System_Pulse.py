import psutil
import time

def print_system_stats():

    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

    disk = psutil.disk_usage('C:')
    print(f"Disk Usage: {disk.percent}%")

while True:
    print_system_stats()
    time.sleep(2)

# Known Issues:
# 1. print functions output compounds endlessly on terminal