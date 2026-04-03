import psutil

def print_system_stats():

    local_cpu_use = psutil.cpu_percent()
    print(f"CPU Usage: {local_cpu_use}%")

    local_memory_use = psutil.virtual_memory()
    print(f"Memory Usage: {local_memory_use.percent}%")

    local_disk_use = psutil.disk_usage('C:')
    print(f"Disk Usage: {local_disk_use.percent}%")

print_system_stats()