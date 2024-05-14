import subprocess
import datetime

def getUser():
    user = subprocess.check_output('whoami').decode('utf-8').rstrip()
    return user

def getHost():
    with open("/etc/hostname", "r") as hostnameFile:
        host = hostnameFile.read()
    host = host.strip()
    return host

def getUptime():
    try:
        uptime = subprocess.check_output(['uptime', '-p']).decode('utf-8').rstrip()
        uptime = uptime[3:]
    except:
        with open("/proc/uptime") as uptimeFile:
            uptime = uptimeFile.read().split(' ')[0]
        uptime = int(round(float(uptime))/60)
        if uptime/60 > 1:
            uptime = str(round(uptime/60)) + ' hours'
        else:
            if uptime < 2:
                uptimeSuffix = ' minute'
            else:
                uptimeSuffix = ' minutes'
            uptime = str(uptime) + uptimeSuffix

    return uptime

def getDistro():
    with open("/etc/os-release") as distroFile:
        distro = distroFile.read().split("\n")[0]
    distro = distro.replace('NAME=', '')[1:-1]
    return distro

def getKernel():
    kernel = subprocess.check_output(['uname', '-r']).decode('utf-8').rstrip()
    kernel = kernel.replace(".x86_64", '')
    kernel = kernel.replace(".aarch64", '')
    return kernel

def getMachineFamily():
    with open("/sys/devices/virtual/dmi/id/product_family") as hardwareIdFile:
        hardwareId = hardwareIdFile.read().strip()
    if hardwareId == 'To be filled by O.E.M.':
        with open("/sys/devices/virtual/dmi/id/board_name") as boardIdFile:
            hardwareId = boardIdFile.read().strip()

    return hardwareId

def getDate():
    fulldate = datetime.datetime.now()
    month = fulldate.strftime("%B")         # = August
    day = fulldate.strftime("%d")           # = 27
    time = fulldate.strftime("%H:%M")       # = 10:45
    return month, day, time
