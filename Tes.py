import numpy as nmp


#####given list (in this topic they should Be all positive integer )
lis=[1,1,2,3,3,5,5,6,4,8,7,9,12,11,11,25,26,21]
max=max(lis)
print(max)
## making a new array based on max number
Myarray= nmp.zeros(max+1,int)

#### loop to to get the list elements  we give any array index (1) it the element matches the index

for x in lis:
 Myarray[x]=1

### our array has been made
### our new list

Newlis=[]

for x in range(len(Myarray)):
 if (Myarray[x]==1):
   Newlis.append(x)

### let see our list with out duplications!!
print(Newlis)
