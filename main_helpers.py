# call these helpers, they'll call other methods from mini_helpers

import sub_helpers
import encoders

# binary is a string, should strictly contain 16 digits
def binaryToHex(sBinary): 

    # this assumes sBinary is in 'X XXXXX XXXXXXXXXX' format
    sBinary = sBinary.replace(' ', '')
    
    sHex = ''
    nibbleArray = [0, 0, 0, 0]

    for eachBit in range(0, 16):
        
        nNibPos = eachBit % 4
        nibbleArray[nNibPos] = int(sBinary[eachBit])

        # already at the end of nibble
        if (eachBit % 4 == 3):
           sHex = sHex + sub_helpers.evaluateNibbleToHex(nibbleArray)

    return sHex

def convertDecimalToBinary(sDecimal):
    
    # bin appends 0b at the start
    sNumberPortion = str(bin(int(sDecimal.split(".")[0])))[2:]

    # we return a string because float cannot handle past a couple # of digits
    if("." in sDecimal):
        sDecimalPortion = sub_helpers.convertDecimalOfDecimalToBinary(sDecimal.split(".")[1])
        sFinalBinary = sNumberPortion + "." + sDecimalPortion
        return sFinalBinary
    
    else:
        return sNumberPortion
        
def inputBinaryMantissaBase2(sMantissa, sBase2):
    
    sMSb = '0'

    if (sMantissa[0] == '-'):
        sMantissa = sMantissa[1:]
        sMSb = '1'

    sMantissa, sBase2 = sub_helpers.onefFormat(sMantissa, sBase2)

    # if denormalized
    nBase2 = int(sBase2)
    if (nBase2 < -15):
        sMantissa, sBase2 = sub_helpers.denormalizedCase(sMantissa, sBase2)
    
    return encoders.encodeToFloatingFormat(sMSb, sMantissa, sBase2)


def inputDecimalBase10(sDecimal, sBase10):
    fDecimal = float(sDecimal) * int(sBase10) * 10
    sBinary = convertDecimalToBinary(str(fDecimal))

    return inputBinaryMantissaBase2(sBinary, 0)