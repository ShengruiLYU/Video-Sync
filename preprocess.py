
import pandas as pd
import glob, os
import datetime
import time
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
 

# set the path to the data directory
path = "C:/Users/Shengrui/Downloads/Trial1/Wearable_Data/files/raw/"


results = pd.DataFrame([])
 
for counter, file in enumerate(glob.glob(path+"*/*.csv")):
	

   
    namedf = pd.read_csv(file, skiprows=0,header = None)
    cols= len(namedf.columns)

    # only process the csv file with 5 cols
    if (cols ==5):
    	
    	namedf1 = pd.read_csv(file,header =None,skiprows=0,usecols=[0,1,2,3,4])
    	
    	results = results.append(namedf1)
 


	
# convert unix time to human readable time
def date_convert(date_unix):
    date = datetime(1970, 1, 1,0,0,0) + timedelta(milliseconds=int(date_unix))

    return date


results[0] = results[0].apply(date_convert)
results = results.drop_duplicates(subset=0)



plt.subplot(3, 1, 1)
plt.plot(results[0],results[2])
plt.gcf().autofmt_xdate()
plt.ylabel('X acceleratation')

plt.subplot(3, 1, 2)
plt.plot(results[0],results[3])
plt.gcf().autofmt_xdate()
plt.ylabel('Y acceleratation')

plt.subplot(3, 1, 3)
plt.plot(results[0],results[4])
plt.gcf().autofmt_xdate()
plt.ylabel('Z acceleratation')

plt.show()

results.to_csv('C:/Users/Shengrui/Desktop/video-sync/combineedTrail1-burak.csv')

