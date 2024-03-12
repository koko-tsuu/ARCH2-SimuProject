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

    # we return a string because float cannot handle past a couple # of digits
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
    
    sMSb = '0'

    if (sMantissa[0] == '-'):
        sMantissa = sMantissa[1:]
        sMSb = '1'

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

    return encodeToFloatingFormat(sMSb, sMantissa, sBase2)

def encodeToFloatingFormat(sMSb, sMantissa, sBase2):
    
    sMantissa, sExponent = encodeExponent(sMantissa, sBase2)
    sTruncatedMantissa = encodeMantissa(sMantissa)
    
    return sMSb + ' ' + sExponent + ' ' + sTruncatedMantissa

def encodeExponent(sMantissa, sBase2):
    nBase2 = int(sBase2) + 15
    
    sExponent = str(bin(nBase2))[2:]

    if (sExponent == '11111' or len(sExponent) > 5):
        sMantissa = '0.0'

    else:
         while(len(sExponent) < 5):
             sExponent = '0' + sExponent

    return sMantissa, sExponent

def encodeMantissa(sMantissa):

    # remove "X."
    sTruncatedMantissa = sMantissa[2:]

    if(len(sTruncatedMantissa) > 10):
        sTruncatedMantissa = sTruncatedMantissa[0:10]
    
    else:
        while(len(sTruncatedMantissa) < 10):
            sTruncatedMantissa = sTruncatedMantissa + '0'
    
    return sTruncatedMantissa


# currently unused, to be tested later
def inputDecimalBase10(decimal, base10):
    decimal = float(decimal) * base10 * 10
    convertDecimalToBinary(decimal)
    return