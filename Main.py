__author__ = 'elizajasin'

import PreProcessing as PreP
import TrainTest as TnT

data = PreP.readData("E:/Kuliah/semester 8/NLP/Tubes/sa-tagged")
case_fold = PreP.caseFolding(data)
print(TnT.tagging(case_fold))