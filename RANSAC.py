from laspy.file import File
import numpy

file = File('./data/Data02.las', mode='r')


def listPoints (inFile=file):
    return file.points
