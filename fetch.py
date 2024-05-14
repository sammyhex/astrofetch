import datetime
import subprocess
import starsigns

class Bash():
    #setup so subprocess(oo).yada yada is just bashCommand(command)
    def getUser():
        user = subprocess.check_output('whoami').decode('utf-8').rstrip()
        return user
    
    def getHost():
        host = subprocess.check_output(['cat', '/etc/hostname']).decode('utf-8').rstrip()
        return host

    def getUptime():
        try:
            uptime = subprocess.check_output(['uptime', '-p']).decode('utf-8').rstrip()
            uptime = uptime[3:]
        except:
            uptime = subprocess.check_output(['cat', '/proc/uptime']).decode('utf-8').rstrip().split(' ')[0]
            uptime = int(round(float(uptime))/60)
            if uptime/60 > 1:
                uptime = str(round(uptime/60)) + ' hours'
            else:
                uptime = str(uptime) + ' minutes'

        return uptime
    
    def getDistro():
        distro = subprocess.check_output(['head', '-1', '/etc/os-release']).decode('utf-8').rstrip()
        distro = distro.replace('NAME=', '')[1:-1]
        return distro

    def getKernel():
        kernel = subprocess.check_output(['uname', '-r']).decode('utf-8').rstrip()
        kernel = kernel.replace(".x86_64", '')
        kernel = kernel.replace(".aarch64", '')
        return kernel

    def getMachineFamily():
        command = 'cat /sys/devices/virtual/dmi/id/product_family'
        command = command.split()
        family = subprocess.check_output(command).decode('utf-8').rstrip()

        if family == 'To be filled by O.E.M.':
            command = 'cat /sys/devices/virtual/dmi/id/board_name'
            command = command.split()
            family = subprocess.check_output(command).decode('utf-8').rstrip()

        return family

class currentDate:
    fulldate = datetime.datetime.now()
    month = fulldate.strftime("%B") # = August
    day = fulldate.strftime("%d") # = 27
    time = fulldate.strftime("%H:%M") # = 10:45
    monthday = (month+day) # = August27

    def __str__(self):
        return f"{self.month} {currentDate.day}"

    def convertDateToSeason(signs): #add error handling
        for sign in signs:
            if sign.startmonth[:3] == currentDate.month[:3]:
                if currentDate.day > sign.startday or currentDate.day == sign.startday:
                    return sign
                else:
                    for sign in signs:
                        if currentDate.month[:3] == sign.endmonth[:3]:
                            return sign

class systemInfo:
    user = Bash.getUser()
    host = Bash.getHost()
    userhost = (user + '@' + host)
    uptime = Bash.getUptime()
    month = currentDate.month
    day = currentDate.day
    time = currentDate.time
    distro = Bash.getDistro()
    kernel = Bash.getKernel()
    machine = Bash.getMachineFamily()

    def boldenText(self, text):
        text = '\033[1m' + text + '\033[0m'
        return text

    def fullsize(self, sign, emoji): #organize this so its quicker, ur running 2 ifs. match maybe
        if len(self.userhost) > len(self.month + self.day + self.time) + 9:
            dashline = ('-' * (len(self.userhost)))
        elif len(self.uptime) + 8 > len(self.month + self.day + self.time) + 9:
            dashline = ('-' * (len(self.uptime) + 8 ))
        else:
            dashline = ('-' * (len(self.month + self.day + self.time) + 9))
        if len(self.machine) + 9 > len(dashline):
            dashline = ('-' * (len(self.machine) + 9))

        systemPortion = (self.userhost, 
            dashline,
            self.boldenText('Date: ') + self.month + ' ' + self.day + ', ' + self.time, 
            dashline, 
            self.boldenText('OS: ') + self.distro, 
            self.boldenText('Kernel: ') + self.kernel, 
            self.boldenText('Uptime: ') + self.uptime, 
            self.boldenText('Machine: ') + self.machine,
            dashline)

        astrologyPortion = (
            self.boldenText('Season: ') + sign.name, 
            self.boldenText('Starts: ') + sign.startmonth + ' ' + sign.startday, 
            self.boldenText('Ends: ') + sign.endmonth + ' ' + sign.endday, 
            self.boldenText('Planet: ') + sign.planet.title(), 
            self.boldenText('Element: ') + sign.element.title(), 
            self.boldenText('Modality: ') + sign.modality.title())

        formattedSystemInfo = (systemPortion + astrologyPortion)

        return formattedSystemInfo

    def smallsize(sign, emoji):
        if not emoji:
            formattedSystemInfo = (
                currentDate.time + 
                ' ' + 
                str(currentDate()) + 
                ', ' + 
                sign.name + 
                ' season.')
        else:
            formattedSystemInfo = (
                currentDate.time +
                ' ' +
                sign.emoji)
        return formattedSystemInfo

    def minimized(sign, emoji):
        if not emoji:
            formattedSystemInfo = sign.name
        else: 
            formattedSystemInfo = sign.emoji
        return formattedSystemInfo
