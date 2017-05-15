__author__ = 'elizajasin'

import os
import re

folder = 'E:/Kuliah/semester 8/NLP/Tubes/sa-tagged'
i = 1
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       s = re.search(r'cmu+(.+)',infilename)
       newname = infilename.replace(str(s.groups()[0]),str(i)+'.txt')
       output = os.rename(infilename, newname)
       i += 1