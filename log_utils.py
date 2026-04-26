# imports function to get system usage stats
from usage import get_system_usage
stats = get_system_usage()

def format_usage(stats): # imports the return values of "get_system_usage()" via the 'stats' variables to be formatted
    return (
        f"CPU Usage: {stats['cpu']}% | "
        f"Memory Usage: {stats['memory']}% | "
        f"Disk Usage: {stats['disk']}%"
    ) # function returns formatted strings (f-strings) representing system usage data