import systeminfo
import build
import starsigns
import search
import findinfo

def matchCliArgs(arguments):
    currentMonth, currentDay, currentTime = findinfo.getDate()
    currentSeason = search.convertDateToStarsign(currentMonth, currentDay)

    if arguments.small:
        build.smallFetch(systeminfo.smallFormat(currentSeason, arguments.unicode))
    elif arguments.mini:
        build.miniFetch(systeminfo.miniFormat(currentSeason, arguments.unicode))
    elif arguments.info:
            search.formatInfoSupplied(arguments.info)
    else:
        build.fullFetch(currentSeason, systeminfo.fullFormat(currentSeason))
