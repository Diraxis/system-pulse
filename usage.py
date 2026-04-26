import psutil # How this tool gets system usage stats
import os     # How this tool knows which operating system is being used

# static variable assignments
is_windows     = os.name == 'nt'
root_path      = 'C:\\' if is_windows else '/'

def get_system_usage(): # gathers CPU, memory, and disk usage values
    return {
        "cpu"    : psutil.cpu_percent(interval = 0.5),
        "memory" : psutil.virtual_memory().percent,
        "disk"   : psutil.disk_usage(root_path).percent,
    } # function returns specified values when called
