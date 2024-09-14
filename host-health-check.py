import psutil
import platform
import socket
import requests

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    return cpu_usage < 80  # Consider healthy if CPU usage is below 80%

def check_memory():
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    return memory.percent < 80  # Consider healthy if memory usage is below 80%

def check_disk():
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")
    return disk.percent < 80  # Consider healthy if disk usage is below 80%

def check_network():
    try:
        # Try to connect to Google's DNS server
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Network: Connected")
        return True
    except OSError:
        print("Network: Disconnected")
        return False

def check_internet():
    try:
        requests.get("http://www.google.com", timeout=3)
        print("Internet: Connected")
        return True
    except requests.ConnectionError:
        print("Internet: Disconnected")
        return False

def main():
    print(f"Host: {platform.node()}")
    print(f"OS: {platform.system()} {platform.release()}")
    
    checks = [
        ("CPU", check_cpu()),
        ("Memory", check_memory()),
        ("Disk", check_disk()),
        ("Network", check_network()),
        ("Internet", check_internet())
    ]
    
    all_healthy = all(result for _, result in checks)
    
    print("\nHealth Check Results:")
    for check, result in checks:
        status = "Healthy" if result else "Unhealthy"
        print(f"{check}: {status}")
    
    print(f"\nOverall Status: {'Healthy' if all_healthy else 'Unhealthy'}")

if __name__ == "__main__":
    main()
