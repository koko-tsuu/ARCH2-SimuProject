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
        nibbleArray[nNibPos] = sub_helpers.to_int(sBinary[eachBit])

        # already at the end of nibble
        if (eachBit % 4 == 3):
           sHex = sHex + sub_helpers.evaluateNibbleToHex(nibbleArray)

    return sHex

        
def inputBinaryMantissaBase2(sMantissa, sBase2):
    if (sub_helpers.inputValidationBase2(sMantissa, sBase2)):
        if(sMantissa.lower() == 'snan'):
            return '0 11111 0100000000'
        elif (sMantissa.lower() == 'qnan'):
            return '0 11111 1000000000'
        else:
            sMSb = '0'

            if (sMantissa[0] == '-'):
                sMantissa = sMantissa[1:]
                sMSb = '1'

            sMantissa, sBase2 = sub_helpers.onefFormat(sMantissa, sBase2)
           
            nBase2 = sub_helpers.to_int(sBase2)
            
            if(nBase2 > 15 or sMantissa > '1.111111111101111'):
                ret = sMSb + ' 11111 0000000000'
                return ret
             # if denormalized
            if (nBase2 < -14):
                sMantissa, sBase2 = sub_helpers.denormalizedCase(sMantissa, sBase2)
      
            return encoders.encodeToFloatingFormat(sMSb, sMantissa, sBase2)
    else:
        return '0 11111 0100000000'

def inputDecimalBase10(sDecimal, sBase10):
    if (sub_helpers.inputValidationBase10(sDecimal, sBase10)):
        if(sDecimal.lower() == 'snan'):
                return '0 11111 0100000000'
            
        elif (sDecimal.lower() == 'qnan'):
                return '0 11111 1000000000'
         
        if (sDecimal[0] == '-'):
            sDecimal = sDecimal[1:]
            sDecimal = sub_helpers.base10Move(sDecimal, sBase10)

            if (sub_helpers.to_int(sDecimal) <= 65519):
                sBinary = sub_helpers.convertDecimalToBinary(sDecimal)
                sBinary = '-' + sBinary
            else:
                 return '1 11111 0000000000'

        else:
            sDecimal = sub_helpers.base10Move(sDecimal, sBase10)
            if (sub_helpers.to_int(sDecimal) <= 65519):
                sBinary = sub_helpers.convertDecimalToBinary(sDecimal)
            else:
                 return '0 11111 0000000000'
        
    else: 
            return '0 11111 0100000000'

    return inputBinaryMantissaBase2(sBinary, 0)