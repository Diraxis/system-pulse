from datetime import datetime
from log_utils import parse_log_line

log_file_path = "log.txt"

# list to hold parsed log entries
entries = []

# reads log file and attempts to parse each line, handling exceptions for malformed lines
with open(file = log_file_path, mode = "r") as file:
    for line in file: # reads every line in the log file
        try:
            entry = parse_log_line(line) # attempts to parse line using function from log_utils.py
            entries.append(entry) # adds parsed data to list of entries
        except ValueError as e: # handles exceptions raised by parse_log_line() and prints error message
            print(f"Error parsing line: {e}")

# checks if any valid entries were parsed, exits if none found
if not entries:
    print("No valid data found.")
    exit()

# calculates average system usage values from parsed log entries
avg_cpu = sum(entry["cpu"] for entry in entries) / len(entries)
avg_memory = sum(entry["memory"] for entry in entries) / len(entries)
avg_disk = sum(entry["disk"] for entry in entries) / len(entries)

# calculates peak system usage values from parsed log entries
max_cpu = max(entry["cpu"] for entry in entries)
max_memory = max(entry["memory"] for entry in entries)
max_disk = max(entry["disk"] for entry in entries)

# calculates monitoring duration from timestamps in parsed log entries
timestamps = [datetime.strptime(entry["timestamp"], "%Y-%m-%d, %H:%M:%S") for entry in entries]
start_time = min(timestamps)
end_time = max(timestamps)
duration = end_time - start_time

# converts duration to hours, minutes, and seconds for display
total_seconds = int(duration.total_seconds())
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# prints summary statistics to the terminal
print(f"Monitoring duration : {hours}h {minutes}m {seconds}s")
print(f"Entries logged      : {len(entries)}")
print(f"Average CPU         : {avg_cpu:.1f}%")
print(f"Peak CPU            : {max_cpu:.1f}%")
print(f"Average Memory      : {avg_memory:.1f}%")
print(f"Peak Memory         : {max_memory:.1f}%")
print(f"Average Disk        : {avg_disk:.1f}%")
print(f"Peak Disk           : {max_disk:.1f}%")