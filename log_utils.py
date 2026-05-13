# imports function to get system usage stats
from usage import get_system_usage
stats = get_system_usage()

def format_usage(stats): # imports the return values of "get_system_usage()" via the 'stats' variables to be formatted
    return (
        f"CPU Usage: {stats['cpu']}% | "
        f"Memory Usage: {stats['memory']}% | "
        f"Disk Usage: {stats['disk']}%"
    ) # function returns formatted strings (f-strings) representing system usage data

def parse_log_line(line):
    
    # validates log line is not empty, raises exception for empty lines
    line = line.strip()
    if not line:
        raise ValueError("Empty log line")

    # breaks structured log line into fields
    parts = line.split(" | ")

    # validates log line structure and value formats, raises exceptions for malformed lines
    if len(parts) != 4:
        raise ValueError("Malformed log line")
    
    # extracts timestamp and cleans usage values from each field
    timestamp = parts[0]
    cpu_str = parts[1].replace("CPU Usage: ", "").replace("%", "")
    memory_str = parts[2].replace("Memory Usage: ", "").replace("%", "")
    disk_str = parts[3].replace("Disk Usage: ", "").replace("%", "")

    # attempts to convert cleaned usage values to floats, raises exceptions for non-numeric values
    try:
        cpu_value = float(cpu_str)
        memory_value = float(memory_str)
        disk_value = float(disk_str)
    except ValueError:
        raise ValueError("Non-numeric log values")

    return {
        "timestamp": timestamp,
        "cpu": cpu_value,
        "memory": memory_value,
        "disk": disk_value
    }