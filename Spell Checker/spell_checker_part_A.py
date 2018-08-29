#!/usr/bin/python3


##################################################################################################################
# Name: Shobhit Srivastava
# Purpose: To process a big dataset and create unigrams, bigrams and other fetures
# Input: none
# Output: A pickled data that contains all the data after processing the document.
# Instruction to run the code:
#	python3 spell_checker_part_A.py
##################################################################################################################


import sys
import codecs
import re
import collections
import operator
import math
import nltk
import time
import pickle
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

#funtion to create ngrams
def ngrams(s, n=2, i=0):
     while len(s[i:i+n]) == n:
         yield s[i:i+n]
         i += 1

#calculating the start time of and the CPU start time
startTime = time.perf_counter()
startCPUTime = time.process_time()
AsciiText = None
wordCount = 0
distintWordCounter = 0
wordDict = {}
x ={}
y = {}
z = {}

#opening the required file
f = open('ap88.txt','r')
BookText = f.readline()
BookTextClean = ''
#Processing the file line by line
while BookText:
    BookTextClean = BookText.replace('AP',' ',1)
    BookTextLower = re.sub(r'[^a-zA-Z ]',' ', BookTextClean).lower();

    AsciiText = re.sub(r'\s+', ' ',BookTextLower)
    angText = re.sub(r'(\w+)',r'<\1>',AsciiText)

    SplitText = angText.split()
    SplitText = sorted(SplitText)
    wordCount = wordCount + len(SplitText)


    #Putting together the distint words
    for item in SplitText:
        if item not in wordDict:
            wordDict[item] = 1
        else:
            wordDict[item] = wordDict[item] + 1

    #making the unigram list
    listUnigram = list(ngrams(angText, n=1))
    listUnigram = sorted(listUnigram)
    #x = collections.Counter(listUnigram)
    for item in listUnigram:
        if item not in x:
            x[item] = 1
        else:
            x[item] = x[item] + 1

    #making the bigram list
    listBigram = list(ngrams(angText, n=2))
    listBigram = sorted(listBigram)
    #y = collections.Counter(listBigram)
    for item in listBigram:
        if item not in y:
            y[item] = 1
        else:
            y[item] = y[item] + 1

    #making the bigram row list
    for item in listBigram:
        if item[0] not in z:
            z[item[0]] = 1
        else:
            z[item[0]] = z[item[0]] + 1

    #reading the next line
    BookText = f.readline()
f.close()

#counting the number of distinct words
distintWordCounter = len(wordDict)

#looking at the end time
endTime = time.perf_counter()
endCPUTime = time.process_time()

#calculating the total elapsed time
totTime = endTime - startTime
totCPUTime = endCPUTime - startCPUTime
#printing the processed data
print("start at elapsed time           {:0.4f},  cpu time    {:0.4f}".format(startTime,startCPUTime))
print("finish reading at elapsed time: {:0.4f},  cpu time    {:0.4f}".format(endTime,endCPUTime))
print("total elapsed time:             {:0.4f},  cpu time    {:0.4f}\n".format(totTime,totCPUTime))


print("Number of words: ", wordCount)

print("Number of types (distinct words): ", distintWordCounter)

print()

print("Unigram counts:")

del x[' ']
for key in x:
    print("{}          {}".format(key,x[key]))

print()

print("Bigram Row:")

del z[' ']
del z['>']
for key in z:
    print("{}*         {}".format(key,z[key]))

print()

print("Bigram counts:")

del y[' <']
del y['> ']
for key in y:
    print("{}          {}".format(key,y[key]))

print()


for key in wordDict:
    print("{} {}".format(key, wordDict[key]))

#creating the list to pickle
listToPickle = []
listToPickle.append(x)
listToPickle.append(y)
listToPickle.append(z)
listToPickle.append(wordDict)

#pickling the list
my_file = open("pickled_data2.dat", 'wb')
pickle.dump(listToPickle, my_file)
