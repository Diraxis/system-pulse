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
def get_system_usage(): # gathers CPU, memory, and disk usage values
    
    cpu_usage    = psutil.cpu_percent(interval = 0.5)
    memory_usage = psutil.virtual_memory().percent
    disk_usage   = psutil.disk_usage(root_path).percent
    
    return cpu_usage, memory_usage, disk_usage # function returns usage values when called

def format_usage(cpu_usage, memory_usage, disk_usage): # imports the return values of "get_system_usage()" to be formatted

    return (
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory_usage}%\n"
        f"Disk Usage: {disk_usage}%"
    ) # function returns formatted strings (f-strings) representing system usage data

# execution program
try: # code that might fail 
    while True:
    
        # OS-independent command
        subprocess.run(clear_terminal, shell = True)
        
        # real-time f-string variable
        timestamp_str = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

        # data refreshes and data is formatted and held in a variable
        cpu_usage, memory_usage, disk_usage = get_system_usage()
        usage_str = format_usage(cpu_usage, memory_usage, disk_usage)

        # formats timestamp and system usage as one package
        entry_log = f"{timestamp_str}\n{usage_str}\n\n"

        # terminal and log outputs
        print(entry_log)
        print(f"Writing to {log_file_path}")

        with open(file = log_file_path, mode = 'a') as file:
            file.write(entry_log)

        # loop execution delay
        time.sleep(2.5)
except KeyboardInterrupt: # exception handling for a specific code failure. (Ctrl+C)
    print("\n[System Pulse v2]: Program ended by user.\n")