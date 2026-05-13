from log_utils import parse_log_line

log_file_path = "log.txt"

# list variables assigned
entries = []
cpu_values = []
memory_values = []
disk_values = []

# access file
with open(file = log_file_path, mode = "r") as file:
    
    # reads every line
    for line in file:

        entries = parse_log_line(line) # calls the function to parse the log line and extract values
        try:
            # evaluates integrity before it collects the extracted values and append them into a list variable
            if (0 <= entries["cpu"] <= 100) and (0 <= entries["memory"] <= 100) and (0 <= entries["disk"] <= 100):
                cpu_values.append(entries["cpu"])
                memory_values.append(entries["memory"])
                disk_values.append(entries["disk"])
        except (IndexError, ValueError):
            continue  # skips malformed lines

# ends program if no data was processed
if not cpu_values:
    print("No data found.")
    exit()

# avg data of system usage
avg_cpu = sum(cpu_values) / len(cpu_values)
avg_memory = sum(memory_values) / len(memory_values)
avg_disk = sum(disk_values) / len(disk_values)

# max data of system usage
max_cpu = max(cpu_values)
max_memory = max(memory_values)
max_disk = max(disk_values)

# analytical readout
print(f"Entries logged : {len(cpu_values)}")
print(f"Average CPU    : {avg_cpu:.1f}%")
print(f"Peak CPU       : {max_cpu:.1f}%")
print(f"Average Memory : {avg_memory:.1f}%")
print(f"Peak Memory    : {max_memory:.1f}%")
print(f"Average Disk   : {avg_disk:.1f}%")
print(f"Peak Disk      : {max_disk:.1f}%")
