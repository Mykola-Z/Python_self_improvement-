# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:55:11 2020

@author: mzly903
"""

file_se= open("input.txt", 'r').readlines() 

dict = {}

number_of_catigories= int(input('How many categories you want to find? \n or just press enter if it\'s 2: ') or '2')
default_categories = [ 'ANIMALS', 'NUMBERS']
i= 0
for i in range(number_of_catigories):
    
    category = input('Please input a category. \n if it\'s {} just press enter: '.format(default_categories[i])) or default_categories[i]
         
    dict[category] = []
 
for i in range(0,len(file_se)):
    
    file_se[i]= file_se[i].replace("\n", "") # a small fuck up

    if str(file_se[i]) in dict:
        y= i
        
    elif file_se[i] not in dict:
        dict[file_se[y]].append(file_se[i])


for i in list(dict):
    print (i)
    print ("\n".join(set(dict[i])))
    