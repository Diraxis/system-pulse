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
    return {
        "cpu"    : psutil.cpu_percent(interval = 0.5),
        "memory" : psutil.virtual_memory().percent,
        "disk"   : psutil.disk_usage(root_path).percent,
    } # function returns usage values when called

def format_usage(stats): # imports the return values of "get_system_usage()" via the 'stats' variables to be formatted
    return (
        f"CPU Usage    : {stats['cpu']}%\n"
        f"Memory Usage : {stats['memory']}%\n"
        f"Disk Usage   : {stats['disk']}%"
    ) # function returns formatted strings (f-strings) representing system usage data

# execution program
try: # main monitoring loop
    while True: 
    
        # OS-independent command
        subprocess.run(clear_terminal, shell = True)
        
        # real-time f-string variable
        timestamp_str = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

        # data refreshes and data is formatted and held in a variable
        stats = get_system_usage()
        usage_str = format_usage(stats)

        # formats timestamp and system usage as one package
        entry_log = f"{timestamp_str}\n{usage_str}"

        # terminal and log outputs
        print(entry_log)

        with open(file = log_file_path, mode = 'a') as file:
            file.write(entry_log + "\n\n")

        # loop execution delay
        time.sleep(2.5)

except KeyboardInterrupt: # handle user interrupt (Ctrl+C) for clean exit
    print("\n[System Pulse v2]: Program ended by user.\n")
