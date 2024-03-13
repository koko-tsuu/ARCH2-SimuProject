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
