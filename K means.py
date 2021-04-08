import math
import matplotlib.pyplot as plt
import numpy as np

#n=int(input("Enter the number of elements:"))
l=[(185,72),(170,56),(168,60),(179,68),(182,72),(188,77),(180,71),(180,70),(183,84),(180,88),(180,67),(177,76)]
c=[]
dist=[]
final=[]
#for i in range (n):
#
    #l.append((int(input("Enter for x")),int(input("Enter the value of y"))))
   
   
k=int(input("Enter the number of clusters:"))

for i in range (k):
    c.append([int(input("Enter for x")),int(input("Enter the value of y"))])
   
#calculate distance between clusters        
#sum1 = 0
#min1=1000
#meanx=[0,0,0]
#meany=[0,0,0]
#cnt=[0,0,0]
m=[]
m1=[]
x=0
x1=[]
y1=[]

for i in range(len(l)):
    x1.append(l[i][0])
    y1.append(l[i][1])
plt.scatter(x1,y1)
plt.show()
while(1):
    x+=1
    final.clear()
    meanx=[0,0,0]
    meany=[0,0,0]
    cnt=[0,0,0]
    m1.clear()
   
    for i in range(len(l)):
        min1=1000
        m.clear()
        for j in range(k):
           
            ecu = math.pow((l[i][0]-c[j][0]),2)+math.pow((l[i][1]-c[j][1]),2)
            ecu=math.sqrt(ecu)
            if min1>ecu:
                min1=ecu
                dist.clear()
                m.clear()
                dist.append((l[i],"cluster"+str(j+1)))
                m.append([i,j])
                   
                   
        final.append(dist[0])
        m1.append(m[0])
   
    print("Iteration",x)
    for i in range(len(l)):
           print(final[i])
   
    for i in range(len(l)):
        for j in range(k):
            if m1[i][1]==j:
                meanx[j]=meanx[j]+l[i][0]
                meany[j]=meany[j]+l[i][1]
                cnt[j]=cnt[j]+1    for j in range(k):
        if(cnt[j]!=0):
            meanx[j]=meanx[j]/cnt[j]
            meany[j]=meany[j]/cnt[j]
    flag=0    
    for j in range(k):
        if c[j][0]==meanx[j] and c[j][1]==meany[j]:        
            flag+=1
    if flag==k:
        break
    else:  
        for j in range(k):
            c[j][0]=meanx[j]
            c[j][1]=meany[j]
           
    print("The new centroids are")
    print(c)

# OUTPUT:
# Enter the number of clusters:2
# Enter for x185
# Enter the value of y72
# Enter for x170
# Enter the value of y56
# Iteration 1

########################### graph will be displayed in output

# ((185, 72), 'cluster1')
# ((170, 56), 'cluster2')
# ((168, 60), 'cluster2')
# ((179, 68), 'cluster1')
# ((182, 72), 'cluster1')
# ((188, 77), 'cluster1')
# ((180, 71), 'cluster1')
# ((180, 70), 'cluster1')
# ((183, 84), 'cluster1')
# ((180, 88), 'cluster1')
# ((180, 67), 'cluster1')
# ((177, 76), 'cluster1')
# The new centroids are
# [[181.4, 74.5], [169.0, 58.0]]
# Iteration 2
# ((185, 72), 'cluster1')
# ((170, 56), 'cluster2')
# ((168, 60), 'cluster2')
# ((179, 68), 'cluster1')
# ((182, 72), 'cluster1')
# ((188, 77), 'cluster1')
# ((180, 71), 'cluster1')
# ((180, 70), 'cluster1')
# ((183, 84), 'cluster1')
# ((180, 88), 'cluster1')
# ((180, 67), 'cluster1')
# ((177, 76), 'cluster1')
