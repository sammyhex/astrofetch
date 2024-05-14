import fetch
import build
import starsigns
import signsearch

class userArguments:
    def __init__(self, arguments):
        self.info = arguments.info
        self.mini = argments.mini
        self.tiny = arguments.tiny
        self.unicode = arguments.unicode

    def checkForConflict(self):
        errorMsg = 'Bad argument.\n See astrofetch -h for usage.'
        if self.small:
            if self.mini or self.info:
                exit(errorMsg)
        if self.mini:
            if self.info:
                exit(errorMsg)

    def callAstrofetch(self):
    #commented stuff needs 2 be where small fetch comes from. build.py NOT fetch.py
            currentSeason = fetch.currentDate.convertDateToSeason(starsigns.signs)
            if self.mini:
                fetch.systemInfo.minimized(currentSeason, self.unicode)
                #build.miniAstrofetch(
                #    currentSeason,
                #    rightSide.minimized(currentSeason))
            elif self.small:
                fetch.systemInfo.smallsize(currentSeason, self.unicode)
                #build.smallAstrofetch(
                #    currentSeason,
                #    rightSide.smallsize(currentSeason))
            if self.info:
                signsearch.formatInfoSupplied(self.info)
            else:
                rightSide = fetch.systemInfo()

                build.fullAstrofetch(
                    currentSeason, 
                    rightSide.fullsize(currentSeason, False))
