#!/bin/python3

import math
import os
import random
import re
import sys

class Wiener():
    def __init__(self, word, YGDash):
        self.word = word
        self.YGDash = YGDash
        self.weight = (int(YGDash[0] == "G") * 100 + int(YGDash[-1] == "G") * 10 + sum(map(word.lower().count, "aeiou")) * 1) * 10000 + sum([(ord(x) - 96) for x in word.lower()])

    def __str__(self):
        return self.YGDash

#
# Complete the 'findMatch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING word
#  2. STRING guesses
#

def findMatch(word, guesses):
    guesses = guesses.split(" ")
    GYYstringList = []

    for guess in guesses:
        FullStr = ["" for x in range(len(word))]

        for letterIndex in range(len(guess)):
            if guess[letterIndex] == word[letterIndex]:
                FullStr[letterIndex] = "G"
            elif guess[letterIndex] in word:
                flag = False
                for letterIndex2 in range(len(guess)):
                    if guess[letterIndex2] == word[letterIndex2] and guess[letterIndex] == guess[letterIndex2]:
                        flag = True
                        break
                if not flag:
                    FullStr[letterIndex] = "Y"
                else:
                    FullStr[letterIndex] = "-"
            else:
                FullStr[letterIndex] = "-"
        
        if "".join(FullStr).replace("-", "") != "":
            GYYstringList.append(Wiener(guess, "".join(FullStr)))
        
    if len(GYYstringList) < 6:
        C = "abcdefghijklmnopqrstuvwxyz"
        for word in guesses:
            for char in word:
                C = C.replace(char, "")
        return C

    Dict = {}
    for Item in GYYstringList:

        gs = str(Item).count("G")

        if gs in Dict:
            Dict[gs].append(Item)
        else:
            Dict.update({gs : [Item]})
    
    Dict = dict(sorted(Dict.items()))

    WeightedDict = {} 
    for key in Dict.keys():
        WeightedDict.update({key : {}})

    for key in Dict:
        for word in Dict[key]:
            yc = str(word).count("Y")

            if yc in WeightedDict[key]:
                WeightedDict[key][yc].append(word)
            else:
                WeightedDict[key].update({yc : [word]})

    for key in WeightedDict:
        for key2 in WeightedDict[key]:
            WeightedDict[key][key2] = sorted(WeightedDict[key][key2], key=lambda x: [x.weight])
        WeightedDict[key] = dict(sorted(WeightedDict[key].items()))

    #Dict = dict(sorted(Dict.items()))
    Final = []
    for key in WeightedDict:
        for key2 in WeightedDict[key]:
            for word in WeightedDict[key][key2]:
                Final.append(word)

    print(list(reversed([str(x) for x in Final])))
    print(list(reversed([str(x.weight) for x in Final])))
    print(list(reversed([str(x.word) for x in Final])))

    return " ".join(reversed([x.word for x in Final[-6:]]))


if __name__ == '__main__':
    print(findMatch("trees", "start eater stack truck tears zones stamp strip sport latex parts kinds lives wings turns hopes meant yearn taste"))