from datetime import datetime

pieces = ["al","bums","bar","ely","be","foul","con","vex","here","by","jig", "saw","tail","or","we","aver"]

words = {"albums", "barely", "befoul", "convex", "hereby", "jigsaw", "tailor", "weaver"}

# using dictionary
def makingOfWords():
    piecesDictionary = {}
    for x in pieces:
        if len(x) in piecesDictionary:
            val = piecesDictionary[len(x)]
            val.append(x)
            piecesDictionary[len(x)] = val
        else:
            piecesDictionary[len(x)] = [x]

    combinationCount = 0
    for x in pieces:
        lenOfPiece = len(x)
        searchableList = piecesDictionary[6 - lenOfPiece]
        for l in searchableList:
            combination = x + l
            print combination
            combinationCount += 1
            if combination in words:
                print 'Found ---->' + combination

    print '\n##############\nCombination count = ' + str(combinationCount) + '\n##############\n'

###
# Program Starts Here
###

makingOfWords()
