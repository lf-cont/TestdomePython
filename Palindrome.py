# Created by Shawn O'Grady on 12/7/17.
# Copyright 2017 Shawn O'Grady. All rights reserved.

 #This code is a practice Python interview question from testdome.com

 #https://www.testdome.com/questions/python/palindrome/7962?visibility=1&skillId=9

 # Problem statement: Write a function that checks if a given word is a palindrome. Character case should be ignored.

 #Passes 3/3 tests
def is_palindrome(word):
        return word.lower()==word.lower()[::-1]

print(is_palindrome('Deleveled'))
