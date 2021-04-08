import numpy as np
import pandas as pd
from itertools import combinations
df = pd.read_csv('apriori.csv',header=None)
df.columns=["Transaction ID","Items"]
print("The Dataset is:")
print(df)
baskets=[]
temp_baskets=[]
for i in range(len(df.values)):
  baskets.append(df.values[i][1])
#print(baskets)
for i in range(len(baskets)):
  temp_baskets.append(baskets[i].split(','))
#print(temp_baskets)
min_sup=3
print("\nMin Support Count is: "+str(min_sup))
counter1={}
counter2={}
counter3={}
for i in range(len(temp_baskets)):
  for j in temp_baskets[i]:
    if j in counter1:
      counter1[j]+=1
    else:
      counter1[j]=1
#print(counter1)
#function to prune the data
def prune(counter1,min_sup):
  for item in list(counter1):
    if counter1[item]<min_sup:
      print("Prunned "+ str(item))
      del counter1[item]
      
      
#fucntion to create combinations
list_of_2_pair=[]
list_of_3_pair=[]
def combine(temp_baskets,n,list_of_n_pair):
  for i in range(len(temp_baskets)):
    list_of_n_pair.append(list(combinations(temp_baskets[i],n)))
    return list_of_n_pair
#print("Two pairs\n")
combine(temp_baskets,2,list_of_2_pair)
#print(list_of_2_pair)
#print("Three pairs\n")
combine(temp_baskets,3,list_of_3_pair)
#print(list_of_3_pair)
print("\nPrunning the Result:")
prune(counter1,min_sup)
#print(counter1)
temp_list2=[]
for i in counter1.keys():
  temp_list2.append(i)
counter_list_2=[]
counter_list_2=list(list(combinations(temp_list2,2)))
#print(counter_list_2)
#print(temp_list2)
for item in counter_list_2:
  #print(type(item))
  for j in range(len(list_of_2_pair)):
    if item in list_of_2_pair[j]:
      if item in counter2:
        counter2[item]+=1
      else:
        counter2[item]=1
#print(counter2)
print("\nPrunning The Result")
prune(counter2,min_sup)
#print(counter2)
temp_list3=[]
counter_list_3=[]
for i in counter2.keys():
  temp_list3.append(i)
#print(temp_list3)
counter_list_3=list(list(combinations(temp_list2,3)))
#print(counter_list_3)
for item in counter_list_3:
  #print(type(item))
  for j in range(len(list_of_3_pair)):
    if item in list_of_3_pair[j]:
      if item in counter3:
        counter3[item]+=1
      else:
        counter3[item]=1
#print(counter3)
print("\nPrunning the result:\n")
prune(counter3,min_sup)
#print(counter3)
print("\nThe Maximum Frequent Set is: ")
for i in counter3.keys():
  print(i)

# Output:
# The Dataset is:
# Transaction ID Items
# 0 t1 i1,i2,i3
# 1 t2 i2,i3,i4
# 2 t3 i4,i5
# 3 t4 i1,i2,i4
# 4 t5 i1,i2,i3,i5
# 5 t6 i1,i2,i3,i4
# Min Support Count is: 3
# Prunning the Result:
# Prunned i5
# Prunning The Result
# Prunned ('i1', 'i4')
# Prunned ('i3', 'i4')
# Prunning the result:
# Prunned ('i1', 'i2', 'i4')
# Prunned ('i1', 'i3', 'i4')
# Prunned ('i2', 'i3', 'i4')
# The Maximum Frequent Set is:
# ('i1', 'i2', 'i3')
