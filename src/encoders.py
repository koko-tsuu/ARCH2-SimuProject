def encodeToFloatingFormat(sMSb, sMantissa, sBase2):
    
    sMantissa, sExponent = encodeExponent(sMantissa, sBase2)
    sTruncatedMantissa = encodeMantissa(sMantissa)
    
    return sMSb + ' ' + sExponent + ' ' + sTruncatedMantissa

def encodeExponent(sMantissa, sBase2):
    nBase2 = int(sBase2) + 15
    
    sExponent = str(bin(nBase2))[2:]

    if (sExponent == '11111' or len(sExponent) > 5):
        sMantissa = '0.0'
        sExponent = '11111'

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