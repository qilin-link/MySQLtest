#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
emp_no
500000-999999999

birth_date
1952-1999

first_name，last_name
字符4-9
首字母大写，in (A,B,C,D,E,F,G,H,J,K,L,M,N,O,P,R,S,T,U,W,Y,Z)

gender
M,F

hire_date
1990-2020
且要>birth_date+20（对年进行计算）
'''

import pymysql
import date
import name
import gender
from time import sleep

config = {
            'host':'10.8.7.51',
            'user':'root',
            'password':'123456',
            'database':'employees',
            'charset':'utf8',
            'port':3306
        }

db = pymysql.connect(**config)
cursor = db.cursor()

#方法三：
l = []
sql = 'insert delayed into employees values(%s,%s,%s,%s,%s,%s)'
for emp_no in range(500367, 500500):
    birth_date = date.birthDate()
    first_name = name.name().capitalize()
    last_name = name.name().capitalize()
    emp_gender = gender.gender()
    hire_date = date.hireDate(birth_date)
    val = (str(emp_no),str(birth_date),str(first_name),str(last_name),str(emp_gender),str(hire_date))
    l.append(val)
    print(l)
    sleep(1)
l = tuple(l)
print(l)
try:
    cursor.executemany(sql,l)
    db.commit()
except Exception as e:
    db.rollback()
    print('Failed:',e)




'''
#方法二：
for emp_no in range(500367, 600000):
    birth_date = date.birthDate()
    first_name = name.name().capitalize()
    last_name = name.name().capitalize()
    emp_gender = gender.gender()
    hire_date = date.hireDate(birth_date)
    try:
        cursor.execute('insert delayed into employees values(%s,%s,%s,%s,%s,%s)',(str(emp_no),str(birth_date),str(first_name),str(last_name),str(emp_gender),str(hire_date)))
        db.commit()
    except Exception as e:
        db.rollback()
        print('Failed:',e)
'''
'''
#方法一：
#emp_no = 500336
while emp_no < 599999:
    birth_date = date.birthDate()
    first_name = name.name().capitalize()
    last_name = name.name().capitalize()
    emp_gender = gender.gender()
    hire_date = date.hireDate(birth_date)
    try:
        cursor.execute('insert delayed into employees values(%s,%s,%s,%s,%s,%s)',(str(emp_no),str(birth_date),str(first_name),str(last_name),str(emp_gender),str(hire_date)))
        db.commit()
    except Exception as e:
        db.rollback()
        print('Failed:',e)
    emp_no += 1
    #sleep(0.3)
'''
#db.commit()
cursor.close()
db.close()