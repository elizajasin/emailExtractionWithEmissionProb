__author__ = 'elizajasin'

import os
from py2casefold import casefold

def readData(path):
    data = []
    directory = os.path.normpath(path)
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                f=open(os.path.join(subdir, file),'r')
                a = f.read()
                # print(f)
                if (file == 0) :
                    print(str(a))
                data.append(str(a))
                f.close()
    return data

def caseFolding (data):
    for i in range(len(data)):
        data[i] = casefold(data[i])
    return data
