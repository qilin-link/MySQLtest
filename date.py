#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from time import mktime,strftime,strptime,localtime
#from datetime import datetime
from random import randint

#随机生成出生日期函数
def birthDate():
    #出生日期时间范围
    birth_date_start = '1970-1-2'
    birth_date_end = '1999-12-31'
    #出生日期转换成时间戳(注意：1970以前无法转换)
    birth_date_start_stamp = mktime(strptime(birth_date_start, '%Y-%m-%d'))
    birth_date_end_stamp = mktime(strptime(birth_date_end,'%Y-%m-%d'))
    #生成随机时间戳
    t_birthdate = randint(birth_date_start_stamp,birth_date_end_stamp)
    #将时间戳转成格式化字符串
    birth_date = strftime('%Y-%m-%d',localtime(t_birthdate))
    #print(birth_date)
    return birth_date

#随机生成雇佣日期函数
def hireDate(birth_date):
    #雇佣日期时间范围
    hire_date_start = '1990-1-1'
    hire_date_end = '2020-1-1'
    #雇佣日期转换成时间戳(注意：1970以前无法转换)
    hire_date_start_stamp = mktime(strptime(hire_date_start, '%Y-%m-%d'))
    hire_date_end_stamp = mktime(strptime(hire_date_end,'%Y-%m-%d'))
    while 1:
        #生成随机时间戳
        t_hiredate = randint(hire_date_start_stamp,hire_date_end_stamp)
        #将时间戳转成格式化字符串
        hire_date = strftime('%Y-%m-%d',localtime(t_hiredate))
        #将传进来的birthd_date参数格式化取年
        birth_date_year = birth_date.split('-')[0]
        hire_date_year = hire_date.split('-')[0]
        #且对年进行计算>birth_date+20
        if (int(hire_date_year) - int(birth_date_year)) > 20:
            return hire_date
        
'''
a = birthDate()
print(a)
b = hireDate(a)
print(b)
'''