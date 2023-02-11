import io
import os
import re
import numpy as np
from os import walk

TEXT_DIR_PATH = "/home/lisic4kin/Documents/Labs/AI/first_lab/texts"

filenames = next(walk(TEXT_DIR_PATH), (None, None, []))[2]

for fileName in filenames:
    inputFile = io.open((TEXT_DIR_PATH + "/" + fileName), mode='r', encoding="ISO-8859-1").read()
    print(inputFile)


# print(type(filenames))
#
# s = 'Hello!@#!%!#&&!*!#$#%@*+_{ world!, sdffjhsd Саня'
# reg = re.compile('[^a-zA-Z, ^а-яА-Я]')
# print(reg.sub('', s))
