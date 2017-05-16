__author__ = 'elizajasin'

import PreProcessing as PreP
import TrainTest as TnT

data = PreP.readData("E:/Kuliah/semester 8/NLP/Tubes/sa-tagged")
case_fold = PreP.caseFolding(data)
ep_time,ep_loc,ep_speak = TnT.train(case_fold,350)
test_time,tes_loc,tes_speak,true_time,true_loc,true_speak = TnT.tes(case_fold,350,ep_time,ep_loc,ep_speak)
print(TnT.akurasi(test_time,tes_loc,tes_speak,true_time,true_loc,true_speak))