import systeminfo
import build
import starsigns
import search
import findinfo

def matchCliArgs(arguments):
    currentMonth, currentDay, currentTime = findinfo.getDate()
    currentSeason = search.convertDateToStarsign(currentMonth, currentDay, False)

    if arguments.small:
        build.smallFetch(systeminfo.smallFormat(currentSeason, arguments.unicode))
    elif arguments.mini:
        build.miniFetch(systeminfo.miniFormat(currentSeason, arguments.unicode))
    elif arguments.info:
        search.processInput(arguments.info, arguments.unicode, True)
    else:
        build.fullFetch(currentSeason, systeminfo.fullFormat(currentSeason))
