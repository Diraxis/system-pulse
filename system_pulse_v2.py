import psutil
import os
import subprocess
import time
from datetime import datetime

is_windows = os.name == 'nt'
root_path = 'C:\\' if is_windows else '/'
clear_command = 'cls' if is_windows else 'clear'
log_file_path = "log.txt"

def get_system_usage_text():

    # Data gathering behaviour (to be migrated into a separate function)
    cpu_usage = psutil.cpu_percent(interval = 0.5)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage(root_path).percent

    return (
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory_usage}%\n"
        f"Disk Usage: {disk_usage}%"
    )
        
while True:

    subprocess.run(clear_command, shell = True)

    timestamp_str = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    usage_text = get_system_usage_text()
    log_entry = f"{timestamp_str}\n{usage_text}\n\n"
    
    print(log_entry)

    with open(file = log_file_path, mode = "a") as file:
        file.write(log_entry)
    time.sleep(2)