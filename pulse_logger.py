# importing modules and classes first for use in the program
import subprocess                   # How this tool runs console commands
import time                         # How this tool delays execution flow of the program
from datetime import datetime       # How this tool gets timestamp data

# importing functions and variables from other programs
from usage import get_system_usage, is_windows
from log_utils import format_usage, stats, usage_str

# static variable assignments
clear_terminal = 'cls' if is_windows else 'clear'
log_file_path  = "log.txt"

# execution program
# main monitoring loop
try: 
    while True: 
    
        # OS-independent command
        subprocess.run(clear_terminal, shell = True)
        
        # real-time f-string variable
        entry_time = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

        # data refreshes and data is formatted and held in a variable
        stats = get_system_usage()
        usage_str = format_usage(stats)

        # formats timestamp and system usage as one package
        entry_log = f"{entry_time} | {usage_str}"

        # terminal and log outputs
        print(entry_log)

        with open(file = log_file_path, mode = 'a') as file:
            file.write(entry_log + "\n")

        # loop execution delay
        time.sleep(2.5)

except KeyboardInterrupt: # handle user interrupt (Ctrl+C) for clean exit
    print("[System Pulse v2]: Program ended by user.\n")
