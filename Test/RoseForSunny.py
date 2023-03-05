def subCase_Bin(binaryString: str) -> str:
    n = 0
    while True:
        nInBinary = str(format(n, "b"))

        if nInBinary in binaryString:
            try:
                if binaryString.index(nInBinary):
                    binaryString = binaryString[:binaryString.index(nInBinary)] + binaryString[binaryString.index(nInBinary) + len(nInBinary):] 

                if binaryString.rindex(nInBinary):
                    binaryString = binaryString[:binaryString.rindex(nInBinary)] + binaryString[binaryString.rindex(nInBinary) + len(nInBinary):]
            except:
                pass

            n += 1
        else:
            break

    return binaryString[1:]

def subCase_Oct(octString: str) -> str:
    n = 0
    while True:
        nInOct = str(format(n, "o"))

        if nInOct in octString:
            try:
                if octString.index(nInOct):
                    octString = octString[:octString.index(nInOct)] + octString[octString.index(nInOct) + len(nInOct):] 

                if octString.rindex(nInOct):
                    octString = octString[:octString.rindex(nInOct)] + octString[octString.rindex(nInOct) + len(nInOct):]
            except:
                pass

            n += 1
        else:
            return int(str(nInOct), 8) - 1


def findLastOctal(s):
    
    binaryAll = ""
    
    for c in s:
        binaryAll += str(format(ord(c), '08b'))
        
    toRepeat = (binToOct(subCase_Bin(binaryAll)))

    return (subCase_Oct(toRepeat))

def binToOct(b) -> str:
    return str(format(int(b, 2), 'o'))

# print("603022200104 - e")

findLastOctal("Roses are red.")