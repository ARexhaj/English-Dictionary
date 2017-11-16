#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:24:52 2017

@author: aurel
"""
#importing dictionary
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    #counting for Uper-Lowercases
    #w = w.lower()
    #counting for non-existing words
    if w in data:
        return data[w]
    elif w.lower() in data:
        return data[w.lower()]
    #counting for spelling errors
    elif len(get_close_matches(w, data.keys())) > 0:
        an=input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w,data.keys())[0]).lower()
        if an=='y':
            return data[get_close_matches(w,data.keys())[1]]
        elif an=='n':
            return "Word doesn't exist. Please double check it."
    else:
        return "We didn't understand your entry."

word = input("Enter word: ")
#formating the output
output= translate(word)
if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)