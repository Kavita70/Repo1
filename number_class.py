# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:37:29 2020

@author: Kavita Bhatnagar

test python file

"""

while True:
    num = int(input('Enter a number: '))
    if num < 20:
        print('Too small!')
    elif num > 50:
        print('Too big!')
    else:
        print('Good number')
        break
