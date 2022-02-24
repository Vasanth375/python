numofout=10  #number of outputs
print(0)#printing 0 and 1
print(1)
k1,k2,k3=0,1,0 #assigning values to operating variables
for i in range(numofout): #range from 0 to 9
    k3=k1+k2 #in first iteration of 0 0=0+1 k3=1
    print(k3) # print(1)
    k1=k2 #transfering k2 data to k1
    k2=k3 #transfering k3 data to k2