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

    totalBinary = 0
    totalBinary += (nibble[0] * 8)
    totalBinary += (nibble[1] * 4)
    totalBinary += (nibble[2] * 2)
    totalBinary += (nibble[3] * 1)

    if(totalBinary > 9):

        totalBinary %= 10
        letter = chr(totalBinary + ord('A'))
        return letter

    else:
        return totalBinary