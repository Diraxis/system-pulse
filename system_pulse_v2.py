# importing modules and classes first for use in the program
import psutil                  # How this tool gets system usage stats
import os                      # How this tool knows which operating system is being used
import subprocess              # How this tool runs console commands
import time                    # How this tool delays execution flow of the program
from datetime import datetime  # How this tool gets timestamp data

# static variable assignments
is_windows     = os.name == 'nt'
root_path      = 'C:\\' if is_windows else '/'
clear_terminal = 'cls' if is_windows else 'clear'
log_file_path  = "log.txt"

# program-specific functions
def system_usage(): # intended to gather three usage states and remember their data as variables
    
    cpu_usage    = psutil.cpu_percent(interval = 0.5)
    memory_usage = psutil.virtual_memory().percent
    disk_usage   = psutil.disk_usage(root_path).percent
    
    return(cpu_usage, memory_usage, disk_usage) # function returns the variables' data when called

def format_usage(cpu_usage, memory_usage, disk_usage): # This function imports the return data of "system_usage()" to be formatted

    return(
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory_usage}%\n"
        f"Disk Usage: {disk_usage}%"
    ) # function returns formatted strings (f-strings) representing system usage data

# execution program
while True:
    
    # OS-independent command
    subprocess.run(clear_terminal, shell = True)
    
    # real-time f-string variable
    timestamp_str = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

    # refresh of variables' data and formats it and remembers via a single variable
    cpu_usage, memory_usage, disk_usage = system_usage()
    usage_str = format_usage(cpu_usage, memory_usage, disk_usage)

    # formats timestamp and system usage as one package
    entry_log = f"{timestamp_str}\n{usage_str}\n\n"

    # terminal and log outputs
    print(entry_log)
    print(f"Writing to {log_file_path}")

    with open (file = log_file_path, mode = 'a') as file:
        file.write(entry_log)

    # loop execution delay
    time.sleep(2.5)