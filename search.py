import starsigns

starsignList = starsigns.signs

def processInput(infoSupplied, useUnicode, printOutput):
    if len(infoSupplied) == 1: 
    #user searched starsign
        infoSupplied = str(infoSupplied)
        formattedInfo = infoSupplied.lower().title()

        convertStarsignToDate(formattedInfo, useUnicode) #pass unicode for ucode+date supplied result?

    else: 
    #user searched date
        for info in infoSupplied:
            if info.isnumeric():
                if int(info) > 31:
                    exit('Date error, higher than 31')
                formattedDay = info
            else:
                info = info[:3]
                formattedMonth = info.lower().title()

        convertDateToStarsign(formattedMonth, formattedDay, printOutput, useUnicode)

def convertDateToStarsign(month, day, printOutput, useUnicode):
# if you type non existant date like feb 31 it still runs, stop it
    monthSupplied = month
    daySupplied = day
    searchSuccess = False
    
    for sign in starsignList:
        if monthSupplied[:3] == sign.startmonth[:3]:
            if daySupplied > sign.startday or daySupplied == sign.startday:
                searchSuccess = True
                foundSign = sign
                break
            else:
                searchSuccess = False

    if not searchSuccess:
        for sign in starsignList:
            if monthSupplied[:3] == sign.endmonth[:3]:
                foundSign = sign
                break

    if printOutput:
        if not useUnicode:
            print(foundSign)
        elif useUnicode:
            print(foundSign.emoji)

    return foundSign

def convertStarsignToDate(infoSupplied, useUnicode):
    infoSupplied = str(infoSupplied[:-2][2:]).lower().title()
    
    for sign in starsignList:
        if infoSupplied == sign.name:
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

    if not useUnicode:
        print('\n'.join(resultForText))
    elif useUnicode:
        print(''.join(resultForUnicode))
