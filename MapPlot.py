from __future__ import print_function
from sys import platform
from os import system
import WalabotAPI as wlbt
#import matplotlib.pyplot as plt
import numpy as np
import csv

wlbt.Init()
wlbt.SetSettingsFolder()
wlbt.ConnectAny()

wlbt.SetProfile(wlbt.PROF_SENSOR)
wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_MTI)

wlbt.Start()
dataArray = np.zeros((39,27), dtype=np.int)
while True:
    wlbt.Trigger()
    targets = wlbt.GetRawImageSlice()
    system('cls' if platform == 'win32' else 'clear')  # clear the terminal
    print("Walabot Connected")
    dataArray = targets[0]
    print(len(targets[0]),len(targets[0][1]))
    f = open('raw_data.csv','w+')
    for item in dataArray:
    	for i in range(len(item)):
    		if i==0:
    			f.write(str(item[i]))
    		else:
    			f.write(','+str(item[i]))
    	f.write('\n')
    f.close()    	
   # f.close()
   # plt.plot(dataArray)
   # plt.draw()
   # plt.pause(0.0001)
   # plt.clf()


wlbt.Stop()
wlbt.Disconnect()