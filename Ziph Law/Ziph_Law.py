#!/usr/bin/python3
#############################################################
#   Name : Shobhit Srivastava
#   Purpose : In this project the primary objective was to find some empirical evidence for (or against) Ziph's Law. Zipf's law states that frequency is 
#	      inversely proportional to rank. For this purpose the frequency of the word length was looked at.
#   Input : Text file(In the provided folder) for which we collect the data
#   Output : Tables with different data about the text file
#   Instruction to run the code :
#       python3 Ziph_Law.py Book.txt > output.txt
#############################################################

import sys
import codecs
import re
import collections
import operator
import math

#Function to print the results in assending format.
def printAccendingOrder(letterCount,rangeStart):
    # prints the character count in accending order
    for key, value in sorted(letterCount.items()):
        if key != ' ' and key != '-' and key != '\'':
            for i in range(rangeStart,123,6):
                if key == chr(i):
                    print("{:<2} {:<7}".format(key,value), end = " ")
    print('\n')

#Function to print the results in the order of their frequency
def printMostCommonOrder(letterCount,rangeStart):
    # prints the character count in the order of frequency
    ctr = 0
    for key, value in letterCount.most_common():
        if key != ' ' and key != '-' and key != '\'':
            ctr += 1
            for i in range(rangeStart,27,6):
                if i == ctr:
                    print("{:<2} {:<7}".format(key,value), end = " ")
    print('\n')

#Function to print the result in decending order of their length
def wordCountDecOrder(letterPerWord, rangeStart):
    # prints the result of the word count with the length of the words
    for key, value in sorted(letterPerWord.items()):
        for i in range(rangeStart,21,4):
            if key == i:
                print("{:>3}{:>6}".format(key,value), end = " ")
    print('\n')

bookLink = sys.argv[1]      #getting the file from the command line
BookText = codecs.open(bookLink, 'r', 'iso-8859-1').read() #getting the text of the file
tempBook = BookText.replace('--','  ') # removing --
bookTextFinal = re.sub('[^a-zA-Z\'\-]',' ',tempBook) # removing all the extra characters
lowerCaseBook = bookTextFinal.lower() #converting to lower case
letterCount = collections.Counter(lowerCaseBook) #counting all the retters
characterCounter = 0
characterRead = 0
distintCharacter = 0

for key, value in sorted(letterCount.items()):
    # counting the characters and the distint characters and how many characters read
    if key != ' ' and key != '-' and key != '\'':
        characterCounter += value
        distintCharacter += 1
    characterRead += value

print('\n')
charValue = 97

for i in range(0,6):
    # calling the function to print in accending order
    printAccendingOrder(letterCount,charValue)
    charValue += 1

print('\n')

charValue = 1
for i in range(0,6):
    # calling the funtion to print in the order of highest to lowest frequency
    printMostCommonOrder(letterCount,charValue)
    charValue += 1
letter_count_per_word = collections.Counter(lowerCaseBook.split(" "))

print('\n')
counter = 0
letterPerWord = {}
for i in range(1,21):
    for key,value in letter_count_per_word.items():
        # counting the letters per word
        if len(key) == i:
            counter += value
    letterPerWord[i] = counter
    counter = 0

charValue = 1
print("len count len count len count len count len count\n")
for i in range(0,4):
    # calling the funtion to print the word length with word frequency
    wordCountDecOrder(letterPerWord, charValue)
    charValue += 1

print('\n')

rank = 0
wordCounter = 0
print("Rank length   freq  len*fre rank*fre lgf/lgr\n")
for key, value in sorted(letterPerWord.items(), key=operator.itemgetter(1), reverse = True):
    # calculating the statistical ressults and printing them
    rank += 1
    lenByFrequency = key*value
    rankByFrequency = rank*value
    ratio = None
    wordCounter += value
    if math.log2(rank) != 0:
        ratio = round(math.log2(value)/math.log2(rank),2)
    else:
        ratio = ''
    print("{:>4}{:>7}{:>7}{:>9}{:>9}{:>8}".format(rank, key, value, lenByFrequency, rankByFrequency, ratio), end = " ")
    print('\n')
print('Total{:>13}'.format(wordCounter))
# Printing the final calculated result
print('Records read:{:>20}'.format(len(BookText.split('\n'))-1))
print('Characters read:{:>17}'.format(characterRead))
print('Characters counted:{:>14}'.format(characterCounter))
print('Words counted:{:>19}'.format(wordCounter))
print('Distint characters:{:>14}'.format(distintCharacter))
