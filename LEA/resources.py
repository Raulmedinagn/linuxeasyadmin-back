import psutil,sys


#Returns the current platform the program is running in
def get_os():
    return str(sys.platform)

#Returns a list with the current processes that are running
#TODO: change list to dictionary, add PID to be able to make operations with them
def get_process_list():
    processList = []

    for p in psutil.process_iter():
        pName = p.name()
        processList.append(str(pName))

    return processList;

#Receives a disk as "/dev/hdx" and returns it currents space, if no argument is passed
#returns the whole disk size
def get_disk_space(disk=None):
    hd_space = None
    if disk is None:
        hd_space = psutil.disk_usage('/')
    else:
        hd_space = psutil.disk_usage(disk)

    return hd_space

#Returns the percentage of the battery
def get_battery_percentage():
    battery = psutil.sensors_battery()
    return str(battery.percent)

def get_ram_usage_percent():
    return psutil.virtual_memory().percent

def get_ram():
    return psutil.virtual_memory()


