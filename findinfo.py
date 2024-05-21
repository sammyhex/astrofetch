import os
import subprocess
import datetime

def getUser():
    user = os.environ['USER']
    return user

def getHost():
    with open("/etc/hostname", "r") as hostnameFile:
        host = hostnameFile.read()
    host = host.strip()
    return host

def getUptime():
    with open("/proc/uptime") as uptimeFile:
        uptime = uptimeFile.read().split(' ')[0]

    rawUptime = round(float(uptime))

    oneMin = 60
    oneHour = 3600
    oneDay = 86400
    oneWeek = 604800
    oneYear = 31556952

    if rawUptime <= oneMin:
        uptimeA = str(rawUptime) + " seconds"
        uptimeB = ''
    elif rawUptime <= oneHour:
        upMinutes = divmod(rawUptime, oneMin)

        uptimeA = str(upMinutes[0]) + " minutes"
        uptimeB = ''
    elif rawUptime <= oneDay:
        upHours = divmod(rawUptime, oneHour)
        upMinutes = divmod(upHours[1], oneMin)

        uptimeA = str(upHours[0]) + " hours"
        uptimeB = str(upMinutes[0]) + " minutes"
    elif rawUptime <= oneWeek:
        upDays = divmod(rawUptime, oneDay)
        upHours = divmod(upDays[1], oneHour)

        uptimeA = str(upDays[0]) + " days"
        uptimeB = str(upHours[0]) + " hours"
    elif rawUptime <= oneYear:
        upWeeks = divmod(rawUptime, oneWeek)
        upDays = divmod(upWeeks[1], oneDay)

        uptimeA = str(upWeeks[0]) + " weeks"
        uptimeB = str(upDays[0]) + " days"
    else:
        upYears = divmod(rawUptime, oneYear)
        upDays = divmod(upYears[1], oneDay)

        uptimeA = str(upYears[0]) + " years"
        uptimeB = str(upDays[0]) + " days"

    uptimePair = [uptimeA, uptimeB]

    count = 0
    for value in uptimePair:
        if value[:2] == '1 ':
            uptimePair[count] = value[:-1]
        elif value[:2] == '0 ':
            uptimePair[count] = ''
        count = count + 1

    if uptimePair[1] == '':
        uptime = str(uptimePair[0])
    else:
        uptime = str(uptimePair[0]) + ', ' + str(uptimePair[1])

    return uptime

def getDistro():
    with open("/etc/os-release") as distroFile:
        distroList = distroFile.read().split("\n")

    NAME1 = distroList[0]
    NAME2 = distroList[1]

    if NAME1[:6] == "PRETTY":
        distro = NAME2
    elif NAME1[:3] == "BUG": #nix-specific
        distro = NAME1[-22:-15]
    else:
        distro = NAME1

    distro = distro.replace('NAME=', '')[1:-1]
    return distro

def getKernel():
    kernel = subprocess.check_output(['uname', '-r']).decode('utf-8').rstrip()
    kernel = kernel.replace(".x86_64", '')
    kernel = kernel.replace(".aarch64", '')
    return kernel

def getDesktopEnv():
    desktopEnv = os.environ['DESKTOP_SESSION']
    match desktopEnv:
        case 'gnome':
            deVersion = subprocess.check_output(['gnome-shell', '--version']).decode('utf-8').rstrip()
            desktopEnv = deVersion.replace('Shell ', '')
        case 'plasmax11' | 'plasma':
            desktopEnv = 'KDE Plasma'
        case 'awesome':
            deVersion = subprocess.check_output(['awesome', '-v']).decode('utf-8').rstrip()
            deVersion = deVersion.split(' ')[1]
            desktopEnv = 'AwesomeWM ' + deVersion[1:]
        case 'xfce':
            deVersion = subprocess.check_output(['xfce4-session', '--version']).decode('utf-8').rstrip()
            deVersion = deVersion.split(' ')[1]
            desktopEnv = 'Xfce ' + deVersion
        case _:
            if desktopEnv == '':
                desktopEnv = ' - '
            else:
                desktopEnv = desktopEnv.lower().title()

    return desktopEnv

def getShell():
    currentShell = ''

    shell = os.environ['SHELL']
    shell = shell.split('/')[-1]

    match shell:
        case 'bash':
            shell = subprocess.check_output(['bash', '--version']).decode('utf-8').rstrip()
            bashVersion = shell.split(' ')[3]
            bashVersionNumber = bashVersion.split('(')
            shell = bashVersionNumber[0]
            currentShell = 'bash ' + shell
        case 'zsh':
            shell = subprocess.check_output(['zsh', '--version']).decode('utf-8').rstrip()
            shell = shell.split(' ')[:-1]
            shell = ' '.join(shell)
            currentShell = currentShell + shell
        case 'fish':
            shell = subprocess.check_output(['fish', '--version']).decode('utf-8').rstrip()
            shell = 'fish ' + shell.split(' ')[-1]
            currentShell = currentShell + shell

    return currentShell

def getMachineFamily():
    with open("/sys/devices/virtual/dmi/id/product_family") as hardwareIdFile:
        hardwareId = hardwareIdFile.read().strip()
    if hardwareId == 'To be filled by O.E.M.':
        with open("/sys/devices/virtual/dmi/id/board_name") as boardIdFile:
            hardwareId = boardIdFile.read().strip()
    elif hardwareId == '':
        with open("/sys/devices/virtual/dmi/id/sys_vendor") as vendorIdFile:
            hardwareId = vendorIdFile.read().strip()

    return hardwareId

def getDate():
    fulldate = datetime.datetime.now()
    month = fulldate.strftime("%B")         # = August
    day = fulldate.strftime("%d")           # = 27
    time = fulldate.strftime("%H:%M")       # = 10:45
    return month, day, time
