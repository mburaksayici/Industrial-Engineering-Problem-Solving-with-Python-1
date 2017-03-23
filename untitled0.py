# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 06:38:57 2017

@author: burak
"""
	

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm

import numpy as np

print("--------------------------")
print("")
print("")
print("")
print("Distance:")
print("New York", "Los Angeles", "Oklahoma")
distancefornewyork = 2900
distanceforlosangeles = 1600    
distanceforoklahoma = 1100
print(distancefornewyork, distanceforlosangeles,distanceforoklahoma)
print("")
print("")
print("")

print("--------------------------")
print("")
print("")
print("")
print("Units for Truck and Train:")
print("Truck, Train")
truckunit = 2000
trainunit = 12000
print("")
print("")
print("")

print("--------------------------")
print("Demand:")
print("New York", "Los Angeles", "Oklahoma")
demandfornewyork = int(25000)
demandforlosangeles = int(35000)
demandforoklahoma = int(20000)
print(demandfornewyork, demandforlosangeles, demandforoklahoma)
print("")
print("")
print("")

print("--------------------------")
def maxvaltrans(demand,unit):
    max = demand/unit
    if ( (int(max) - float(max) != 0 )):
            max = int(max + ( 1 - np.abs(float(max)-int(max))   ))
            return max
    print(max)
     
  
    
    
    
print("For New York, We are trying to optimize for lowest cost using best")
print("option of transportation:")
print("For New York, we can use ")
print(maxvaltrans(demandfornewyork, truckunit))
print("truck and")
print(maxvaltrans(demandfornewyork,trainunit))
print("train if we use just one of them")
print("But we will optimize it, so truck-train number can not be more than")
print("these. Our method to find optimum values is testing our formulas and")
print("Finding the minimal amount of them.")

print("For New York;")


print("New York", "Los Angeles", "Oklahoma")
checker = int(0)

trainlistfornewyork = range((1+maxvaltrans(demandfornewyork,trainunit)))
trucklistfornewyork = range((1+maxvaltrans(demandfornewyork,truckunit)))

costsfornewyork = []
for i in range (1+maxvaltrans(demandfornewyork,trainunit)):
    
    costsfornewyork.append(trainlistfornewyork[checker]*(100 + 0.4*distancefornewyork) + trucklistfornewyork*(3200 + 0.05*distancefornewyork))
    checker = checker +1


print(".")
print(costsfornewyork)
print(".")

print("")
print("")
print("")



print("")
print("")
print("")

print("--------------------------")
print("Train Costs:")
print("New York", "Los Angeles", "Oklahoma")
train =  (demand/12000)*(3200+0.05*distance)
print(".")
print(train)
print(".")

print("")
print("")
print("")


print("--------------------------")

print("Comparison of Truck and Train Costs in Bar Charts")


# data to plot
n_groups = 3
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, truck, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Truck')
 
rects2 = plt.bar(index + bar_width, train, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Train')
 
plt.xlabel('Cities')
plt.ylabel('Truck/Train Cost')
plt.title('Truck/Train Comparison')
plt.xticks(index + bar_width, ('New York', 'Los Angeles', 'Oklahoma'))
plt.legend()
 
plt.tight_layout()
plt.show()