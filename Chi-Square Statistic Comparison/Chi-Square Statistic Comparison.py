#!/usr/bin/python3
##################################################################################################################
# Name: Shobhit Srivastava
# Homework 1
# Due Date: 02/20/2018
# Purpose: To understand the basic concepts of python3
# Input: Two urls of the files from project gutenberg
# Output: Chi-Square value
# Instruction to run the code:
#	python3 hw1.py https://www.gutenberg.org/files/1342/1342-0.txt https://www.gutenberg.org/files/2650/2650-0.txt
##################################################################################################################
import sys
import urllib.request
import re
import unicodedata

if len(sys.argv) != 3:
	print('****ERROR**** Two files are required')
	sys.exit(0)
url = sys.argv[1]
f = urllib.request.urlopen(url)
book1 = f.read().decode()
numCharBook1 = len(book1)
numLinesBook1 = len(book1.split('\n'))
numVowelsBook1 = 0
numConsonantsBook1 = 0
numLetterBook1 = 0

for i in book1.lower():
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		numVowelsBook1 += 1
	if unicodedata.category(i)[0] == 'L':
		numLetterBook1 += 1
numConsonantsBook1 = numLetterBook1 - numVowelsBook1
print('**************Results for Pride and Prejudice************\n')
print('Number of lines : ', numLinesBook1 - 1)
print('Number of character : ', numCharBook1 - book1.count('\n'))
print('Number of vowels are :', numVowelsBook1)
print('Number of consonants are : ', numConsonantsBook1)# - book1.count(' ') - book1.count('\n'))
print('Number of letters : ', numLetterBook1)#numVowelsBook1 + numConsonantsBook1)
print('percentage vowel : %.2f \n' % ((numVowelsBook1/(numVowelsBook1 + numConsonantsBook1))*100))


url2 = sys.argv[2]
b2 = urllib.request.urlopen(url2)
book2 = b2.read().decode('utf-8')
numCharBook2 = len(book2)
numLinesBook2 = len(book2.split('\n'))
numVowelsBook2 = 0
numConsonantsBook2 = 0
numLetterBook2 = 0
for i in book2.lower():
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		numVowelsBook2 += 1
	elif(i==u'\u00e9' or i==u'\u00e2' or i==u'\u00ea' or i==u'\u00ee' or i==u'\u00f4' or i==u'\u00fb' or i==u'\u00e0' or i==u'\u00e8' or i==u'\u00f9' or i==u'\u00eb' or i==u'\u00ef' or i==u'\u00fc'):
		numVowelsBook2 += 1
	if unicodedata.category(i)[0] == 'L':
		numLetterBook2 += 1
numConsonantsBook2 = numLetterBook2 - numVowelsBook2
print('**************Results for Du côté de chez Swann ************\n')
print('Number of lines : ', numLinesBook2 - 1)
print('Number of character : ', numCharBook2 - book2.count('\n'))
print('Number of vowels are :', numVowelsBook2)
print('Number of consonants are : ', numConsonantsBook2)
print('Number of letters : ', numLetterBook2)
print('percentage vowel : %.2f\n' % ((numVowelsBook2/(numVowelsBook2 + numConsonantsBook2))*100))

totConsonantBook1 = ((numConsonantsBook1 + numVowelsBook1) * (numConsonantsBook1 + numConsonantsBook2))/((numConsonantsBook1 + numVowelsBook1) + (numConsonantsBook2 + numVowelsBook2))
totConsonantBook2 = ((numConsonantsBook2 + numVowelsBook2) * (numConsonantsBook1 + numConsonantsBook2))/((numConsonantsBook1 + numVowelsBook1) + (numConsonantsBook2 + numVowelsBook2))
totVowelBook1 = ((numConsonantsBook1 + numVowelsBook1) * (numVowelsBook1 + numVowelsBook2))/((numConsonantsBook1 + numVowelsBook1) + (numConsonantsBook2 + numVowelsBook2))
totVowelBook2 = ((numConsonantsBook2+ numVowelsBook2) * (numVowelsBook1 + numVowelsBook2))/((numConsonantsBook1 + numVowelsBook1) + (numConsonantsBook2 + numVowelsBook2))
print('Book1: Pride and Prejudice')
print(" Consonants : %.2f" % totConsonantBook1 )
print(" Vowels :     %.2f\n" % totVowelBook1)
print('Book2: Du côté de chez Swann')
print(" Consonants : %.2f" % totConsonantBook2)
print(" Vowels :     %.2f\n" % totVowelBook2)

chiSquare = (((numVowelsBook1 - totVowelBook1)**2) / totVowelBook1) + (((numVowelsBook2 - totVowelBook2)**2) / totVowelBook2) + (((numConsonantsBook1 - totConsonantBook1)**2) / totConsonantBook1) + (((numConsonantsBook2 - totConsonantBook2)**2) / totConsonantBook2)
print(" Chi-Square :     %.2f" % chiSquare)
