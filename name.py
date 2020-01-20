#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from random import randint

#letter_list = ['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','R','S','T','U','W','Y','Z']
letter_list = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','r','s','t','u','w','y','z']

def randLetter():
    i = randint(0,len(letter_list)-1)
    return letter_list[i]

def name():
    name = ''
    l = randint(4,9)
    n = 0
    while n < l:
        letter = randLetter()
        name += letter 
        n += 1
    return name
        
     
