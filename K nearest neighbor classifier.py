import math
a=[]
ps=0;
fl=0
n=int(input("Enter the no of records: "))
print("Enter the records \n")
for i in range(0,n):
    print('Name  Maths-marks  Comp-Marks Result')
    name, mks_1,mks_2,result=input().split()
    mks_1=int(mks_1)
    mks_2=int(mks_2)
    a.append([0,name,mks_1,mks_2,result])
       
    
print('\nName  Maths-marks  Comp-Marks Result')
for i in range(0,n):
    print(f'{a[i][1]}\t{a[i][2]} \t   {a[i][3]} \t   {a[i][4]}')
    
k=int(input("\nEnter the value of k: "))
print('Enter the query you want to predict')
print('Name  Maths-Marks  Comp-Marks ')
name, mks_1,mks_2=input().split()
mks_1=int(mks_1)
mks_2=int(mks_2)
for i in range(0,n):
    d=math.sqrt(((mks_1-a[i][2])**2)+((mks_2-a[i][3])**2))
    a[i][0]=d
a.sort()
for i in range(0,k):
     print(f'{a[i]}')

for i in range(0,k):
    if a[i][4]=='pass':
        ps=ps+1
    else:
        fl=fl+1
        
if ps>fl:
    result="pass"
else:
    result="fail"
    
print('\npredicted query')   
print('Name  math-marks  cs-marks result')
print(f'{name}\t{mks_1} \t   {mks_2} \t   {result}')

# OUTPUT:
# Enter the no of records: 11
# Enter the records 

# Name  Maths-marks  Comp-Marks Result
# praj 25 20 pass
# Name  Maths-marks  Comp-Marks Result
# bharat 25 25 pass
# Name  Maths-marks  Comp-Marks Result
# sourabh 20 20 pass
# Name  Maths-marks  Comp-Marks Result
# ram 5 10 fail
# Name  Maths-marks  Comp-Marks Result
# sam 15 16 pass
# Name  Maths-marks  Comp-Marks Result
# syam 18 19 pass
# Name  Maths-marks  Comp-Marks Result
# bai 3 4 fail
# Name  Maths-marks  Comp-Marks Result
# lol 10 10 pass 
# Name  Maths-marks  Comp-Marks Result
# abc 19 19 pass
# Name  Maths-marks  Comp-Marks Result
# wow 7 7 fail
# Name  Maths-marks  Comp-Marks Result
# babu 3 1 fail

# Name  Maths-marks  Comp-Marks Result
# praj	      25 	   20 	   pass

# bharat	25 	   25 	   pass
# sourabh	20 	   20 	   pass
# ram	      5 	   10 	   fail
# sam	      15 	   16 	   pass
# syam	      18 	   19 	   pass
# bai	      3 	   4 	         fail
# lol	      10 	   10 	   pass
# abc	      19 	   19 	   pass
# wow	      7 	   7 	        fail
# babu	      3 	   1 	        fail

# Enter the value of k: 3
# Enter the query you want to predict
# Name  Maths-Marks  Comp-Marks 
# boi 12 10
# [2.0, 'lol', 10, 10, 'pass']
# [5.830951894845301, 'wow', 7, 7, 'fail']
# [6.708203932499369, 'sam', 15, 16, 'pass']

# predicted query
# Name  math-marks  cs-marks result
# boi	12 	       10 	     pass

