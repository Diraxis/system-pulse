# This is my first official program
# Git Branch: Master

import psutil

# Print the usage of the cpu; memory; disk
# Let's remember the state of each usage too

local_cpu_use = psutil.cpu_percent()
print(f"CPU Usage: {local_cpu_use}%")

local_memory_use = psutil.virtual_memory()
print(f"Memory Usage: {local_memory_use.percent}%") # Note:The following feature is cut (out of scope) >> f"({local_memory_use.used/1024/1024/1024}/{local_memory_use.total/1024/1024/1024} GB)")

local_disk_use = psutil.disk_usage('C:')
print(f"Disk Usage: {local_disk_use.percent}%")