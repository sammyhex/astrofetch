import datetime
import findinfo
import starsigns

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
    user = findinfo.getUser()
    host = findinfo.getHost()
    userhost = (user + '@' + host)
    uptime = findinfo.getUptime()
    month = currentDate.month
    day = currentDate.day
    time = currentDate.time
    distro = findinfo.getDistro()
    kernel = findinfo.getKernel()
    machine = findinfo.getMachineFamily()

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
