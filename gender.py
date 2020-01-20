#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from random import randint

gender_list = ['M','F']

def gender():
    i = randint(0,len(gender_list)-1)
    return gender_list[i]


