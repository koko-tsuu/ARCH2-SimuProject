def evaluateNibbleToHex(nibbleArray):

    # this is just converting binary to decimal
    nTotalBinary = 0
    nTotalBinary += (nibbleArray[0] * 8)
    nTotalBinary += (nibbleArray[1] * 4)
    nTotalBinary += (nibbleArray[2] * 2)
    nTotalBinary += (nibbleArray[3] * 1)

    if(nTotalBinary > 9):

        nTotalBinary %= 10
        cLetter = chr(nTotalBinary + ord('A'))    # using ASCII
        return cLetter

    else:
        return str(nTotalBinary)
    

def denormalizedCase(sMantissa, sBase2):
    nBase2 = to_int(sBase2)

    # -14 is the min
    nTimesToMove = (abs(nBase2 + 14)-1)

    sMantissa = sMantissa.replace('.', '')

    for x in range(0, nTimesToMove):
        sMantissa = '0' + sMantissa

    sMantissa = '0.' + sMantissa

    return sMantissa, str(-15)

def onefFormat(sMantissa, sBase2):
     # conversion for easy data manipulation
    nBase2 = to_int(sBase2)

    # is it 1.f format?
    if (sMantissa[0:2] != '1.'):
        if("." in sMantissa):
            if(sMantissa[0:2] == '0.'):
                if("1" in sMantissa):
                    n1Index = sMantissa.index('1')
                    sMantissa = '1.' + sMantissa[n1Index+1:]
                    
                    # minus 1 because decimal point was included in finding index
                    nBase2 -= (n1Index - 1)
                else:
                    return "0.0", '0'

            else:    
                # we need to move it manually using strings
                nDecimalPointIndex = sMantissa.index('.')

                # -1 because we don't move the decimal point beyond MSb
                nBase2Moves = nDecimalPointIndex - 1

                sMantissa = sMantissa.replace('.', '')
                sMantissa = "1." + sMantissa[1:]

                nBase2 = nBase2 + nBase2Moves
        else:
            if("1" in sMantissa):
                # -1 because we don't move the decimal point beyond MSb
                nBase2Moves = len(sMantissa) - 1
                
                sMantissa = "1." + sMantissa[1:]
                nBase2 = nBase2 + nBase2Moves
            else:
                  return "0.0", '0'
    
    return sMantissa, str(nBase2)


# floating points are finicky so we'll do it manually
def base10Move(sDecimal, sBase10):

    nBase10 = to_int(sBase10)
     
    if(not("." in sDecimal)):
        sDecimal = sDecimal + '.'
        
    # move to right
    # consider if we don't have any numbers after
    if (nBase10 > 0):
        
        while(nBase10 != 0):

            # example: 2.01
            #          2(0)1
            nDecimalPointIndex = sDecimal.index('.') 

            sDecimal = sDecimal.replace('.', '')
            nLastDigitIndex = len(sDecimal) - 1
            
            # need to append a zero
            if (nLastDigitIndex == (nDecimalPointIndex-1)):
                sDecimal = sDecimal[0:] + '0.'

            else:
                sDecimal = sDecimal[0:nDecimalPointIndex+1] + '.' + sDecimal[nDecimalPointIndex+1:]
                
            nBase10 -= 1

    # move to left: not done
    elif (nBase10 < 0):
         while(nBase10 != 0):

            nDecimalPointIndex = sDecimal.index('.')
            sDecimal = sDecimal.replace('.', '')

            # need to append a zero
            # case: X.XXXXX
            if (nDecimalPointIndex == 1):
                 sDecimal = "0." + sDecimal
            
            else:
                sDecimal = sDecimal[0:nDecimalPointIndex-1] + '.' + sDecimal[nDecimalPointIndex-1:]

            nBase10 += 1
    
    return sDecimal

def convertDecimalToBinary(sDecimal):

    # bin appends 0b at the start
    sNumberPortion = str(bin(to_int(sDecimal.split(".")[0])))[2:]

    # we return a string because float cannot handle past a couple # of digits
    if("." in sDecimal):
        sDecimalPortion = convertDecimalOfDecimalToBinary(sDecimal.split(".")[1])
        sFinalBinary = sNumberPortion + "." + sDecimalPortion
        return sFinalBinary

    else:
        return sNumberPortion
    
def convertDecimalOfDecimalToBinary(sDecimal):

    sFinalBinary = ''
    sDecimalToMultiply = "0." + sDecimal

    # max 30 mantissa digits
    x = 0

    while (x <= 30):
        # not 0.000
        if (sDecimalToMultiply != '0.0' and sDecimalToMultiply != '0.'):

            # multiply by 2
            sDecimalToMultiply = multiplicationDecimal(sDecimalToMultiply)

            # get MSb (x).xxx
            cMSb = sDecimalToMultiply[0]
            if (x == 0):
                x = x + int(cMSb)
            else:
                x = x + 1

            # replace MSb to 0
            sDecimalToMultiply = '0' + sDecimalToMultiply[1:]

            # append to string
            sFinalBinary = sFinalBinary + cMSb
        else:
            x = x + 1

    # return string         
    return sFinalBinary


def multiplicationDecimal(sDecimal):
    nCarryover = 0
    sTemp = ''
    sProduct = ''

    for x in range(len(sDecimal)-1, 1, -1):
        sTemp = str(nCarryover + int(sDecimal[x]) * 2)
        if (len(sTemp) > 1):
            # last digit
            if (x == 2):
                sProduct = sTemp[0] + '.' + sTemp[1] + sProduct
            else:   
                nCarryover = int(sTemp[0])
                sProduct = sTemp[1] + sProduct

        else:
            nCarryover = 0
            if (x == 2):
                sProduct =  '0.' + sTemp[0] + sProduct
            else:
                sProduct = sTemp[0] + sProduct

    return sProduct


def inputValidationBase2(sMantissa, sBase2):
    sBase2 = str(sBase2)
    sMantissa = str(sMantissa)
    nDotCounter = 0

    if (sMantissa.lower() == 'snan' or sMantissa.lower() == 'qnan'):
        return True

    if (sMantissa[0] == '-'):
        sMantissa = sMantissa[1:]

    if (sBase2[0] == '-'):
        sBase2 = sBase2[1:]
    
    for x in sMantissa:
        if (x == '.' and nDotCounter == 0):
            nDotCounter+=1

        elif (x != '0' and x != '1'):
            return False
    
    try:
        for x in sBase2:
            int(x)
    except:
        return False
    
    return True


def inputValidationBase10(sDecimal, sBase10):
    sBase10 = str(sBase10)
    nDotCounter = 0

    if (sDecimal.lower() == 'snan' or sDecimal.lower() == 'qnan'):
        return True
    
    if (sDecimal[0] == '-'):
        sDecimal = sDecimal[1:]

    if (sBase10[0] == '-'):
        sBase10 = sBase10[1:]
    
    try:
        for x in sDecimal:
            if (x == '.' and nDotCounter == 0):
                nDotCounter+=1
            else:
                int(x)
    except:
        return False
    
    try:
        for x in sBase10:
            int(x)
    except:
        return False
    
    return True

def to_int(sNumber):

    nSign = 1
    sNumber = str(sNumber)

    if (sNumber[0] == '-'):
        nSign = -1
        sNumber = sNumber[1:]

    nFinalNumber = 0

    if('.' in sNumber):
        nIndex = sNumber.index('.')
        nSecondIncrementor = 0

        # first half
        for x in range(nIndex, 0, -1):
            nTensCounter = pow(10, x-1)
            nFinalNumber = nFinalNumber + (nTensCounter * int(sNumber[nSecondIncrementor]))
            nSecondIncrementor+=1

        for x in range(nIndex+1, len(sNumber), 1):
            nTensCounter = pow(10, (nIndex-x))
            nFinalNumber = nFinalNumber + (nTensCounter * int(sNumber[x]))

        
    else:
        for x in range((len(sNumber)-1), -1, -1):
            nTensCounter = pow(10, len(sNumber) - 1 - x)
            nFinalNumber = nFinalNumber + (nTensCounter * int(sNumber[x]))

    return nFinalNumber * nSign

def toRoundUp(sTruncatedMantissa):
    LsbIsEven = (sTruncatedMantissa[9] == '0')
    sRoundToEven = sTruncatedMantissa[10:]
    toRound = False

     # first element is 1 (10...0 -> round to even)
    if (sRoundToEven[0] == '1'):
        toRound = True

        # check all elements 
        for x in range(1, len(sRoundToEven)):
            # not a zero
            if (sRoundToEven[x] != '0'):
                break

            # last element and is 0
            elif (sRoundToEven[x] == '0' and x == (len(sRoundToEven)-1)):
                if (LsbIsEven):
                    toRound = False
    return toRound

def handleCarryOver(sTruncatedMantissa):
    handledCarryOver = False
    sFinal = ''
    x = 0
    copyIndex = -1

    sTemp = sTruncatedMantissa[0:10]

    # handle carry over
    while(not handledCarryOver and x <= 9):
        if (sTemp[9-x] == '0' and not handledCarryOver):
            handledCarryOver = True
            copyIndex = (9-x)

        x+=1
    # no more space
    if (not handledCarryOver):
        sFinal = '1000000000'

    else:
        sFinal = sTemp[0:copyIndex] + '1' 

    while(len(sFinal) <= 9):
        sFinal = sFinal + '0'
        
    return sFinal
