# file interaction location
log_file_path = "log.txt"

# list variables assigned
cpu_values = []
memory_values = []
disk_values = []

# access file
with open(file = log_file_path, mode = "r") as file:
    
    # reads every line
    for line in file:

        # cleans whitespace and skips empty lines
        line = line.strip()
        if not line:
            continue
        
        # breaks structured line into fields
        parts = line.split(" | ")

        # extracts numerical values from each field
        cpu_value = float(parts[1].replace("CPU Usage: ", "").replace("%", ""))
        memory_value = float(parts[2].replace("Memory Usage: ", "").replace("%", ""))
        disk_value = float(parts[3].replace("Disk Usage: ", "").replace("%", ""))

        # collect the extracted values and append them into a list variable
        cpu_values.append(cpu_value)
        memory_values.append(memory_value)
        disk_values.append(disk_value)

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
