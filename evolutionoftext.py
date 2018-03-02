"""
Created on Fri Mar 02 17:54:56 2018

@author: terre
"""'
#Created by Dylan Randall
import string
import random
import time

def initChars():
    characters = []
    for alphaLow in string.ascii_lowercase:
        characters.append(alphaLow)

    for digs in string.digits:
        characters.append(digs)

    for alphaHigh in string.ascii_uppercase:
        characters.append(alphaHigh)

    symbols = ' .,!?;:'

    for symbol in symbols:
        characters.append(symbol)

    return characters

def tryMatchText(textIn):
    characters = initChars()
    targetText = textIn

    attemptThis = ''.join(random.choice(characters) for i in range(len(targetText)))
    attemptNext = ''
    completed = False
    generation = 0

    while completed == False:
        print(attemptThis)
        attemptNext = ''
        completed = True

        for i in range(len(targetText)):
            if attemptThis[i] != targetText[i]:
                completed = False

                if attemptThis[i] != ' ':
                    if attemptThis[i] not in targetText:
                        if attemptThis[i] in characters:
                            characters.remove(attemptThis[i])
                    
                attemptNext += random.choice(characters)
            else:
                attemptNext += targetText[i]

        generation += 1
        attemptThis = attemptNext

    print("Target Matched! That took "+str(generation)+" generation(s)")

text = input("Enter target text: ")
tryMatchText(text)