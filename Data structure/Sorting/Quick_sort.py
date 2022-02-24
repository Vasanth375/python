'''
Program to print array number to the particular pivot element only
'''
arr=[1,2,3,4,5,6,7,8]
pivot=4
# for i,v in enumerate(arr):
#     if v==pivot:
#         break
#     else:
#         print(v)
n=len(arr)-1
for i in range(n,0):
    print(arr[i])