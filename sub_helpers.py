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
    
def convertDecimalOfDecimalToBinary(sDecimal):

    sFinalBinary = ''
    fDecimalToMultiply = float("0." + sDecimal)

    # max 10 mantissa digits
    for x in range(0, 10):

        # not 0.000
        if (fDecimalToMultiply != 0):
           
            # multiply by 2
            fDecimalToMultiply *= 2

            # get MSb (x).xxx
            cMSb = str(fDecimalToMultiply)[0]

            # replace MSb to 0
            sZeroDotDecimal = '0' + str(fDecimalToMultiply)[1:]

            # for next iteration
            fDecimalToMultiply = float(sZeroDotDecimal)

            # append to string
            sFinalBinary = sFinalBinary + cMSb

    # return string             
    return sFinalBinary

def denormalizedCase(sMantissa, sBase2):
    nBase2 = int(sBase2)

    # -1 because of additional zero, because '0.' will be appended
    nTimesToMove = (abs(nBase2 + 15) - 1)

    sMantissa = sMantissa.replace('.', '')

    for x in range(0, nTimesToMove):
        sMantissa = '0' + sMantissa

    sMantissa = '0.' + sMantissa
    
    return sMantissa, str(-15)


def onefFormat(sMantissa, sBase2):
     # conversion for easy data manipulation
    nBase2 = int(sBase2)

    # is it 1.f format?
    if (sMantissa[0:2] != '1.'):
        if("." in sMantissa):
            if(sMantissa[0:2] == '0.'):

                n1Index = sMantissa.index('1')
                sMantissa = '1.' + sMantissa[n1Index+1:]
                
                # minus 1 because decimal point was included in finding index
                nBase2 -= (n1Index - 1)

            else:    
                # we need to move it manually using strings
                nDecimalPointIndex = sMantissa.index('.')

                # -1 because we don't move the decimal point beyond MSb
                nBase2Moves = nDecimalPointIndex - 1

                sMantissa = sMantissa.replace('.', '')
                sMantissa = "1." + sMantissa[1:]

                nBase2 = nBase2 + nBase2Moves
        else:
            # -1 because we don't move the decimal point beyond MSb
            nBase2Moves = len(sMantissa) - 1
            
            sMantissa = "1." + sMantissa[1:]
            nBase2 = nBase2 + nBase2Moves
    
    return sMantissa, str(nBase2)


# floating points are finicky so we'll do it manually
def base10Move(sDecimal, sBase10):

    nBase10 = int(sBase10)
     
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
    sNumberPortion = str(bin(int(sDecimal.split(".")[0])))[2:]

    # we return a string because float cannot handle past a couple # of digits
    if("." in sDecimal):
        sDecimalPortion = convertDecimalOfDecimalToBinary(sDecimal.split(".")[1])
        sFinalBinary = sNumberPortion + "." + sDecimalPortion
        return sFinalBinary
    
    else:
        return sNumberPortion

def inputValidationBase2(sMantissa, sBase2):
    sBase2 = str(sBase2)
    nDotCounter = 0

    if (sMantissa == 'sNaN' or sMantissa == 'qNaN' or sMantissa == 'snan' or sMantissa == 'qnan'):
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

    if (sDecimal == 'sNaN' or sDecimal == 'qNaN' or sDecimal == 'snan' or sDecimal == 'qnan'):
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