import psutil

def print_system_stats():

    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

    disk = psutil.disk_usage('C:')
    print(f"Disk Usage: {disk.percent}%")

print_system_stats()