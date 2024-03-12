# binary is a string, should strictly contain 16 digits
def binaryToHex(sBinary): 
    
    nibbleArray = [0, 0, 0, 0]
    for eachBit in range(0, 16):
        
        nibPos = eachBit % 4
        nibbleArray[nibPos] = int(sBinary[eachBit])

        # already at the end of nibble
        if (eachBit % 4 == 3):
            evaluateNibbleToHex(nibbleArray)

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
        return nTotalBinary
    
def convertDecimalToBinary(sDecimal):
    
    # remove 0b
    sNumberPortion = str(bin(int(sDecimal.split(".")[0])))[2:]

    # we return a string because float cannot handle past 10 decimal digits
    if("." in sDecimal):
        sDecimalPortion = convertDecimalOfDecimalToBinary(sDecimal.split(".")[1])
        sFinalBinary = sNumberPortion + "." + sDecimalPortion
        return sFinalBinary
    else:
        return sNumberPortion
        
    
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

def inputBinaryMantissaBase2(sMantissa, sBase2):

    # insert code here later if exponent value is beyond the allowed version or less than

    # conversion for easy data manip
    nBase2 = int(sBase2)

    # is it 1.f format?
    if (sMantissa[0:1] != '1.'):
        
        if("." in sMantissa):
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


# currently unused, to be tested later
def inputDecimalBase10(decimal, base10):
    decimal = float(decimal) * base10 * 10
    convertDecimalToBinary(decimal)
    return