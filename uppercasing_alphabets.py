# -*- coding: utf-8 -*-
"""
Created on August 11th, 2017

@author: Pardis Ranjbar
E-mail: pardis.ranjbar@gmail.com
#==============================================================================
# This code gets a word from user, and changes all lower cases to upper cases.
If there is an upper case already, it doesn't change it.
If there's an invalid character, it tells the user.
#==============================================================================
"""
word=input('enter the word here:\n')
while str.isalpha(word) == True:  #while all characters in "word" are alphabets:
    for char in word:
        if 97<=ord(char)<=122:  #lower case ASCII codes
            print(chr(ord(char)-32), end='') #calculates the upper case of the letters's ASCII code
        elif 65<=ord(char)<=90: #upper case ASCII code
            print (char, end='') #just prints the letter as it is
    break # if every character was an alphabet, then this program is done
else: #if any character is not an alphabet
    print("Enter alphabets ONLY!")
