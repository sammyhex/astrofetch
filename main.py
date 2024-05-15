import systeminfo
import build
import starsigns
import search
import findinfo

def matchCliArgs(arguments):
    showResult = False
    useUnicode = False

    currentMonth, currentDay, currentTime = findinfo.getDate()
    currentSeason = search.convertDateToStarsign(currentMonth, currentDay, showResult, useUnicode)

    if arguments.small:
        build.smallFetch(systeminfo.smallFormat(currentSeason, arguments.unicode))
    elif arguments.mini:
        build.miniFetch(systeminfo.miniFormat(currentSeason, arguments.unicode))
    elif arguments.info:
        showResult = True
        search.processInput(arguments.info, arguments.unicode, showResult)
    else:
        build.fullFetch(currentSeason, systeminfo.fullFormat(currentSeason))
