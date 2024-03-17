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

        
def inputBinaryMantissaBase2(sMantissa, sBase2):
    if (sub_helpers.inputValidationBase2(sMantissa, sBase2)):
        if(sMantissa == 'sNaN' or sMantissa == 'snan'):
            return '0 11111 0100000000'
        elif (sMantissa == 'qNaN' or sMantissa == 'qnan'):
            return '0 11111 1000000000'
        else:
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
    else:
        return '0 11111 0100000000'

def inputDecimalBase10(sDecimal, sBase10):
    if (sDecimal[0] == '-'):
        sDecimal = sDecimal[1:]
        
        if (sub_helpers.inputValidationBase10(sDecimal, sBase10)):

            if(sDecimal == 'sNaN' or sDecimal == 'snan'):
                return '0 11111 0100000000'
            
            elif (sDecimal == 'qNaN' or sDecimal == 'qnan'):
                return '0 11111 1000000000'
            
            sDecimal = sub_helpers.base10Move(sDecimal, sBase10)
            sBinary = sub_helpers.convertDecimalToBinary(sDecimal)
            sBinary = '-' + sBinary
            
        else: 
            return '0 11111 0100000000'
    
    else:
        sDecimal = sub_helpers.base10Move(sDecimal, sBase10)
        sBinary = sub_helpers.convertDecimalToBinary(sDecimal)

    return inputBinaryMantissaBase2(sBinary, 0)