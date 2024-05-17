import datetime
import findinfo
import starsigns

user = findinfo.getUser()
host = findinfo.getHost()
userhost = (user + '@' + host)
uptime = findinfo.getUptime()
month, day, time = findinfo.getDate()
distro = findinfo.getDistro()
kernel = findinfo.getKernel()
machine = findinfo.getMachineFamily()

def boldenText(text):
    text = '\033[1m' + text + '\033[0m'
    return text

def fullFormat(sign): #organize this so its quicker, ur running 2 ifs. match maybe
    if len(userhost) > len(month + day + time) + 9:
        dashline = ('-' * (len(userhost)))
    elif len(uptime) + 8 > len(month + day + time) + 9:
        dashline = ('-' * (len(uptime) + 8 ))
    else:
        dashline = ('-' * (len(month + day + time) + 9))
    if len(machine) + 9 > len(dashline):
        dashline = ('-' * (len(machine) + 9))
    elif len(kernel) + 9 > len(dashline):
        dashline = ('-' * (len(kernel) + 9))

    systemPortion = (
        userhost, 
        dashline,
        boldenText('Date: ') + month + ' ' + day + ', ' + time, 
        dashline, 
        boldenText('OS: ') + distro, 
        boldenText('Kernel: ') + kernel, 
        boldenText('Uptime: ') + uptime, 
        boldenText('Machine: ') + machine,
        dashline)

    astrologyPortion = (
        boldenText('Season: ') + sign.name, 
        boldenText('Starts: ') + sign.startmonth + ' ' + sign.startday, 
        boldenText('Ends: ') + sign.endmonth + ' ' + sign.endday, 
        boldenText('Planet: ') + sign.planet.title(), 
        boldenText('Element: ') + sign.element.title(), 
        boldenText('Modality: ') + sign.modality.title())

    formattedSystemInfo = (systemPortion + astrologyPortion)

    return formattedSystemInfo

def smallFormat(sign, useUnicode):
    if not useUnicode:
        formattedSystemInfo = (
            time + 
            ' ' + 
            str(month + ' ' + day) + 
            ', ' + 
            sign.name + 
            ' season.')
    else:
        formattedSystemInfo = (
            time +
            ' ' +
            sign.emoji)

    return formattedSystemInfo

def miniFormat(sign, useUnicode):
    if not useUnicode:
        formattedSystemInfo = sign.name
    else: 
        formattedSystemInfo = sign.emoji

    return formattedSystemInfo
