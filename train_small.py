'''
Train Cascade
=============
Uses opencv_traincascade to train a classifier.
'''

import sys, os

OPENCV_BIN = "C:/Users/san/PycharmProjects/PythonOpenCV/classifier_training/"
PROGRAM = "opencv_traincascade.exe"
INPUT_FILE = "p.vec"
OUTPUT_CASCADE_DIR = "./"
PARAMS = {  "-data": OUTPUT_CASCADE_DIR,
            "-vec": INPUT_FILE,
            "-bg": "p.txt",
            "-w": 24,
            "-h": 24,
            "-precalcValBufSize": 7168,
            "-precalcIdxBuffSize": 3072,
            "-numPos": 80,
            "-numNeg": 109,
            "featureType": "HAAR",
            "-mode": "ALL"}
command = OPENCV_BIN + PROGRAM
for key in PARAMS:
    command = command + " " + key + " " + str(PARAMS[key])
command = command + ' -numThreads 12 -maxFalseAlarmRate 0.5 -minHitRate 0.995000 -maxFalseAlarmRate 0.500000 -weightTrimRate 0.999 -maxDepth 1 -maxWeakCount 100'
print("Executing {0}".format(command))
os.system(command)