import io
import re
from collections import Counter
from os import walk
import json

TEXT_DIR_PATH = "/home/lisic4kin/Documents/Labs/AI/first_lab/texts"

filenames = next(walk(TEXT_DIR_PATH), (None, None, []))[2]
resultFileString = ""
for fileName in filenames:
    inputFile = io.open((TEXT_DIR_PATH + "/" + fileName), mode='r', encoding="windows-1251").read()
    resultFileString += re.sub(r'[^а-яА-Я\s]', '', inputFile) + " "
result = dict(Counter(resultFileString.split()))
result = sorted(result.items(), key=lambda item: item[1], reverse=True)

with open(r"Result.txt", "w") as outputFile:
    for key, value in result:
        outputFile.write(str(key) + ":" + str(value) + "\n")
