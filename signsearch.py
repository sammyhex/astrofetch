import starsigns

starsignList = starsigns.signs

def formatInfoSupplied(infoSupplied):
#split infoSupplied?
    if len(infoSupplied) == 1:
        infoSupplied = str(infoSupplied)
        formattedInfo = infoSupplied.lower().title()

        convertStarsignToDate(formattedInfo)

    else: 
        for info in infoSupplied:
            if info.isnumeric():
                if int(info) > 31:
                    exit('Date error, higher than 31')
                formattedDay = info
            else:
                info = info[:3]
                formattedMonth = info.lower().title()

        convertDateToStarsign(formattedMonth, formattedDay)

def convertDateToStarsign(month, day):
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
                exit("Date error!")

    if not searchSuccess:
        for sign in starsignList:
            if monthSupplied[:3] == sign.endmonth[:3]:
                if daySupplied < sign.endday:
                    searchSuccess = True
                    foundSign = sign
                    break
                else:
                    exit('Date Error!')

    if not searchSuccess:
        print('Unknown argument: ' + infoSupplied + '\nSee astrofetch -h for usage.')

    returnInfo = (monthSupplied + ' ' + daySupplied + ': ', 
        foundSign.name + ' season.\n',
        str(foundSign))

    print(''.join(returnInfo))
    return returnInfo

def convertStarsignToDate(infoSupplied):
    infoSupplied = str(infoSupplied[:-2][2:]).lower().title()
    
    for sign in starsignList:
        if infoSupplied == sign.name:
            fullInfo = [str(sign),
                'Planet: ' + sign.planet.title(), 
                'Element: ' + sign.element.title(),
                'Modality: ' + sign.modality.title()]
            break

    if fullInfo:
        print('\n'.join(fullInfo))
    else:
        print('Unknown argument: ' + infoSupplied + '\nSee astrofetch -h for usage.')
        exit()
