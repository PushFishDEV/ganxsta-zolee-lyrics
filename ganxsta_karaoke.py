#!/bin/python
import time
import sys
import os

print("i> Select which Ganxsta Zolee song you will karaoke to!")
res = []
# Iterate directory
for file in os.listdir("."):
    # check only text files
    if file.endswith('.txt'):
        res.append(file)

i=0
for r in res:
        print(str(i)+"> "+r)
        i+=1

fid = int(input("?> Type file ID: "))

print("File "+res[fid]+" selected, good choice!")

print("Be ready for karaoke to ganxsta zolee")

print("In ", end="")
sys.stdout.flush()
time.sleep(0.3)

print("3", end="..")
sys.stdout.flush()
time.sleep(1)

print("2", end="..")
sys.stdout.flush()
time.sleep(1)

print("1", end="..")
sys.stdout.flush()
time.sleep(1)

print("GO!")
