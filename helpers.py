# binary is a string, should strictly contain 16 digits
def binaryToHex(binary): 
    
    nibble = [0, 0, 0, 0]
    for eachBit in range(0, 16):
        
        nibPos = eachBit % 4
        nibble[nibPos] = int(binary[eachBit])

        # already at the end of nibble
        if (eachBit % 4 == 3):
            evaluateNibbleToHex(nibble)

def evaluateNibbleToHex(nibble):

    # this is just converting binary to decimal
    totalBinary = 0
    totalBinary += (nibble[0] * 8)
    totalBinary += (nibble[1] * 4)
    totalBinary += (nibble[2] * 2)
    totalBinary += (nibble[3] * 1)

    if(totalBinary > 9):

        totalBinary %= 10
        letter = chr(totalBinary + ord('A'))    # using ASCII
        return letter

    else:
        return totalBinary
    
def convertDecimalToBinary(decimal):
    
    # remove 0b
    sNumberPortion = str(bin(int(decimal.split(".")[0])))[2:]

    # we return a string because float cannot handle past 10 decimal digits
    if("." in decimal):
        sDecimalPortion = convertDecimalOfDecimalToBinary(decimal.split(".")[1])
        sFinalBinary = sNumberPortion + "." + sDecimalPortion
        return sFinalBinary
    else:
        return sNumberPortion
        
    

def convertDecimalOfDecimalToBinary(decimal):

    sFinalBinary = ''
    fDecimalToMultiply = float("0." + decimal)

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

def inputBinaryMantissaBase2(mantissa, base2):
    pass

def inputDecimalBase10(decimal, base10):
    decimal = float(decimal) * base10 * 10
    convertDecimalToBinary(decimal)
    return