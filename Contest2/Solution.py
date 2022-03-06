import string
alphabet = list(string.ascii_lowercase)

def Encode(fibs, key, decoded):
    Return = ""
    
    for letterindex in range(len(decoded)):
        NewLetter = alphabet[(alphabet.index(key) + fibs[letterindex]) % len(alphabet)]
        Return += str(ord(NewLetter) * 3 + ord(decoded[letterindex])) + " "

    return Return

def Decode(fibs, key, encoded):

    encoded = [int(x) for x in encoded.split(" ")]

    Return = ""

    for numberindex in range(len(encoded)):
        StrippedNumber = encoded[numberindex] - 3 * ord(alphabet[(alphabet.index(key) + fibs[numberindex]) % len(alphabet)])
        Return += chr(StrippedNumber)

    return Return

def fibCypher(option, num1, num2, key, msg):

    msg = msg.strip()

    Fibs = [num1, num2]
    for i in range(2, len(msg)):
        Fibs.append(Fibs[i - 1] + Fibs[i - 2])

    for i in range(1, len(Fibs), 2):
        Fibs[i] = Fibs[i] * -1

    if (option == 'E'):
        return Encode(Fibs, key, msg)
    else:
        return Decode(Fibs, key, msg)
    
if __name__ == '__main__':
    print(fibCypher("D", 6, 1, "z", "379 479 341 447 448 329 381 397 402 402 395 462 404 383 425 434 446 383 469 468 405 464 408 449 433 329 390 425 429 395 446 420 449 368 417 397 363 363 395 429 443 383 464 395 446 344 408 458 445 431 335 367 402 394 475 419 391 "))