Consider the following data:
D1: Illegal mining should be stopped.
D2: Mining of data is crucial for analysis
D3: Knowledge can be extracted from huge corpus.
D4: Data Mining and pattern mining are useful.

import numpy as np
import re    ###### regex function for splittint string into words
from math import log

D1="Illegal mining should be stopped"
D2="Mining of data is crucial for analysis"
D3="Knowledge can be extracted from huge corpus"
D4="Data Mining and pattern mining are useful"

D1=D1.lower()    #### convert full line to lowercase
D2=D2.lower()
d3=D3.lower()

D4=D4.lower()

datalist=[D1,D2,D3,D4]

d1=re.findall(r'\w+',datalist[0])    #### '\w+'  is a regular expression
d2=re.findall(r'\w+',datalist[1])
d3=re.findall(r'\w+',datalist[2])
d4=re.findall(r'\w+',datalist[3])

datalist2=[d1,d2,d3,d4]
bag_of_data=[]
for line in datalist2:
    for word in line:
        if word not in bag_of_data:          
            bag_of_data.append(word)
            

d1vec=[]
d2vec=[]
d3vec=[]
d4vec=[]
datavec=[d1vec,d2vec,d3vec,d4vec]

for word in bag_of_data:
    wordfrequency=0
    temporarylist=[]
    for lines in datalist2:
        if lines.count(word)>0:
            temporarylist.append(lines.count(word))
            wordfrequency=wordfrequency+lines.count(word)
        else:
            temporarylist.append(0)
    print(temporarylist)
    print(word)
#   print(wordfrequency)    
    numerator=len(datalist2)
    denominator=wordfrequency
    l=log((numerator/denominator),10)
    for i in range(len(datalist2)):
        tf_value=temporarylist[i]
        #print(l)
        datavec[i].append((tf_value/len(datalist[i])) * l)
print(datavec) 
# [1, 0, 0, 0]
# illegal
# [1, 1, 0, 2]
# mining
# [1, 0, 0, 0]
# should
# [1, 0, 1, 0]
# be
# [1, 0, 0, 0]
# stopped
# [0, 1, 0, 0]
# of
# [0, 1, 0, 1]
# data
# [0, 1, 0, 0]
# is
# [0, 1, 0, 0]
# crucial
# [0, 1, 0, 0]
# for
# [0, 1, 0, 0]
# analysis
# [0, 0, 1, 0]
# Knowledge
# [0, 0, 1, 0]
# can
# [0, 0, 1, 0]
# extracted
# [0, 0, 1, 0]
# from
# [0, 0, 1, 0]
# huge
# [0, 0, 1, 0]
# corpus
# [0, 0, 0, 1]
# and
# [0, 0, 0, 1]
# pattern
# [0, 0, 0, 1]
# are
# [0, 0, 0, 1]
# Useful

# [[0.01881437472899882, 0.0, 0.01881437472899882, 0.00940718736449941, 0.01881437472899882, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.015843683982314796, 0.007921841991157398, 0.015843683982314796, 0.015843683982314796, 0.015843683982314796, 0.015843683982314796, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.007000697573580956, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.014001395147161913, 0.014001395147161913, 0.014001395147161913, 0.014001395147161913, 0.014001395147161913, 0.014001395147161913, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.007342195016194662, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.014684390032389324, 0.014684390032389324, 0.014684390032389324, 0.014684390032389324]]

def cosine(list1,list2):
    dot=0
    l1=0
    l2=0
    for i in range(len(bag_of_data)):    ###for dot product
        dot=dot + (list1[i] * list2[i])
        l1=l1 + (list1[i] * list1[i])
        l2=l2 + (list2[i] * list2[i])
    l1dist=math.sqrt(l1)
    l2dist=math.sqrt(l2)
    cos=dot/(l1dist * l2dist)
    print("cosine distance is : ",cos)

def euclid(list1,list2):
    sumation=0
    for i in range(len(bag_of_data)):
        sumation=sumation + (list1[i] * list2[i])
    distance=math.sqrt(sumation)
    print("euclid distance is : " ,distance)

def smc_jaccard(list1,list2):
    M10=0
    M01=0
    M11=0
    M00=0
    for i in range(len(bag_of_data)):
        if list1[i]==list2[i]:
            if list1[i]==0:
                M00=M00+1
            else:
                M11=M11+1
        else:
            if list1[i]>list2[i]:
                M10=M10+1
            else:
                M01=M01+1
                
    smc=(M11 +M00)/(M11 + M00 + M10 + M01)
    print("smc : ",smc)
    jaccard=M11/(M01 + M10 + M11)
    print("jaccard : ", jaccard)

smc_jaccard(d1vec,d2vec)
euclid(d2vec,d4vec)
cosine(d1vec,d3vec)

# smc :  0.5238095238095238
# jaccard :  0.0
# [0.0, 0.0, 0.0, 0.0, 0.0, 0.015843683982314796, 0.007921841991157398, 0.015843683982314796, 0.015843683982314796, 0.015843683982314796, 0.015843683982314796, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# euclid distance is :  0.007626513540705048
# cosine distance is :  0.05547001962252291

