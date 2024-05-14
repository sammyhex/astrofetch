import parsecli
import astrofetch

if __name__ == '__main__':
    astrofetch.userArguments.checkForConflict(parsecli.args)
    astrofetch.userArguments.callAstrofetch(parsecli.args)
