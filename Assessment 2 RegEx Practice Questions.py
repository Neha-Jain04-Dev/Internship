#!/usr/bin/env python
# coding: utf-8

# # Assessment 2

# # RegEx Practice Questions

# In[5]:


import re


# #Question 1- Write a RegEx pattern in python program to check that a string contains only a certain set of 
# characters (in this case a-z, A-Z and 0-9).

# In[6]:


if __name__ == '__main__':
    string = input("Enter any string:")
    RegExPattern = re.compile("[a-zA-Z0-9]+")

    if RegExPattern.fullmatch(string) is not None:  
        print("Found match: ",string)
    else:
        print("No match",string) 


# #Question 2- Write a RegEx pattern that matches a string that has an a followed by zero or more b's

# In[7]:


def RegEx_Pattern_match(string):
    
    RegExPattern = '^a(b*)$'
    if re.search(RegExPattern, string):
        print("Found a match!")
    else:
        print('Not matched!')
        
        
String=input("Enter any string:") 
RegEx_Pattern_match(String)


# #Question 3-  Write a RegEx pattern that matches a string that has an a followed by one or more b's

# In[9]:


def RegEx_Pattern_match(string):
    
    RegExPattern = 'ab+?'
    if re.search(RegExPattern, string):
        print("Found a match!")
    else:
        print('Not matched!')
        
        
String=input("Enter any string:") 
RegEx_Pattern_match(String)


# #Question 4- Write a RegEx pattern that matches a string that has an a followed by zero or one 'b'

# In[11]:


def RegEx_Pattern_match(string):
    
    RegExPattern = 'ab?'
    if re.search(RegExPattern, string):
        print("Found a match!")
    else:
        print('Not matched!')
        
        
String=input("Enter any string:") 
RegEx_Pattern_match(String)


# #Question 5-Write a RegEx pattern in python program that matches a string that has an a followed by three 'b'.

# In[6]:


def RegEx_Pattern_match(string):
    
    RegExPattern = 'ab{3}'
    if re.search(RegExPattern, string):
        print("Found a match!")
    else:
        print('Not matched!')
        
        
String=input("Enter any string:") 
RegEx_Pattern_match(String)


# #Question 6- Write a RegEx pattern in python program that matches a string that has an a followed by two to three 'b'.

# In[7]:


def RegEx_Pattern_match(string):
    
    RegExPattern = 'ab{2,3}'
    if re.search(RegExPattern, string):
        print("Found a match!")
    else:
        print('Not matched!')
        
        
String=input("Enter any string:") 
RegEx_Pattern_match(String)


# #Question 7- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# In[8]:


def RegEx_Pattern_match(string):
    
    RegExPattern = 'a.*?b$'
    if re.search(RegExPattern, string):
        print("Found a match!")
    else:
        print('Not matched!')
        
        
String=input("Enter any string:") 
RegEx_Pattern_match(String)


# #Question 8-Write a RegEx pattern in python program that matches a word at the beginning of a string.

# In[10]:


def RegEx_Pattern_match(string):
    
    RegExPattern = '^\w+'
    if re.search(RegExPattern, string):
        return ("Found a match!")
    else:
            return('Not matched!')
        
        
String=input("Enter any string:") 
RegEx_Pattern_match(String)


# #Question 9-Write a RegEx pattern in python program that matches a word at the end of a string.

# In[11]:


def RegEx_Pattern_match(string):
    
    RegExPattern = '\w+\S*$'
    if re.search(RegExPattern, string):
        print("Found a match!")
    else:
        print('Not matched!')
        
        

String=input("Enter any string:") 
RegEx_Pattern_match(String)


# #Question 10-Write a RegEx pattern in python program to find all words that are 4 digits long in a string.Sample text- 01 0132 231875 1458 301 2725. Expected output-['0132', '1458', '2725']
# 

# In[12]:


import re

def RegEx_Pattern_match(string):
    RegExPattern =  r'\b\w{4}\b'
    print(re.findall(RegExPattern, string))
       
        
        
String=input("Enter any string:") 
RegEx_Pattern_match(String)


# In[ ]:




