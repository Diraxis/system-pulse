import psutil
import os
import subprocess
import time

is_windows = os.name == 'nt'
root_path = 'C:\\' if is_windows else '/'
clear_command = 'cls' if is_windows else 'clear'

def print_system_usage():

    # Data gathering behaviour (to be migrated into a separate function)
    cpu_usage = psutil.cpu_percent(interval = 0.5)
    memory_usage = psutil.virtual_memory()
    disk_usage = psutil.disk_usage(root_path)

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage.percent}%")
    print(f"Disk Usage: {disk_usage.percent}%")

while True:

    subprocess.run(clear_command, shell = True)
    print_system_usage()
    time.sleep(2)