import starsigns

starsignList = starsigns.signs

infoFormatErr = 'wrong wrONG WRONG!!'
invalidSearchErr = 'astrofetch: invalid search term'
invalidDateErr = 'astrofetch: invalid date'
promptForHelp = 'see astrofetch -h for usage'
    
def processInput(infoSupplied, useUnicode, printOutput):
    #Error handling
    if len(infoSupplied) > 2:
        print(invalidSearchErr)
        exit(promptForHelp)

    for info in infoSupplied:
        if info.isnumeric():
            if int(info) > 31 or int(info) < 1:
                print(invalidDateErr)
                exit(promptForHelp)
        elif len(info) > 11:
            print(invalidSearchErr)
            exit(promptForHelp)

    #1 arg = user likely searched starsign
    if len(infoSupplied) == 1: 
        infoSupplied = str(infoSupplied)
        formattedInfo = infoSupplied.lower().title()

        convertStarsignToDate(formattedInfo, useUnicode)

    #2 args = user likely searched date
    elif len(infoSupplied) == 2: 
        for info in infoSupplied:
            if info.isnumeric():
                formattedDay = info
            else:
                info = info[:3]
                formattedMonth = info.lower().title()

        convertDateToStarsign(formattedMonth, formattedDay, printOutput, useUnicode)
    
def convertDateToStarsign(month, day, printOutput, useUnicode):
    monthSupplied = month[:3]
    daySupplied = day
    day30 = ['Feb', 'Apr', 'Jun', 'Sep', 'Nov']
    searchSuccess = False

    if monthSupplied in day30:
        if int(daySupplied) > 30:
            print(invalidDateErr)
            exit(promptForHelp)
        elif int(daySupplied) > 29 and monthSupplied == 'Feb':
            print(invalidDateErr)
            exit(promptForHelp)
    
    for sign in starsignList:
        if monthSupplied == sign.startmonth[:3]:
            if daySupplied > sign.startday or daySupplied == sign.startday:
                searchSuccess = True
                foundSign = sign
                break

    if not searchSuccess:
        for sign in starsignList:
            if monthSupplied == sign.endmonth[:3]:
                searchSuccess = True
                foundSign = sign
                break
    
    if not searchSuccess:
        print(invalidDateErr)
        exit(promptForHelp)

    if printOutput:
        if not useUnicode:
            print(foundSign)
        elif useUnicode:
            print(foundSign.emoji)
    else:
        return foundSign

def convertStarsignToDate(infoSupplied, useUnicode):
    infoSupplied = str(infoSupplied[:-2][2:]).lower().title()
    searchSuccess = False
    
    for sign in starsignList:
        if infoSupplied == sign.name:
            searchSuccess = True
            resultForUnicode = [
                sign.emoji, 
                ' ', 
                sign.startmonth[:3], 
                ' ', 
                sign.startday, 
                ' -> ', 
                sign.endmonth[:3], 
                ' ', 
                sign.endday]
            resultForText = [
                str(sign),
                'Planet: ' + sign.planet.title(), 
                'Element: ' + sign.element.title(),
                'Modality: ' + sign.modality.title()]
            break
    
    if not searchSuccess:
        print(invalidSearchErr)
        exit(promptForHelp)

    if not useUnicode:
        print('\n'.join(resultForText))
    elif useUnicode:
        print(''.join(resultForUnicode))
