def binary(arr, x, low, high):
  '''Binary Search is method used to search for an item using iterative method'''
  while low <= high:
    mid = int((low+high)/2)
    
    if x == arr[mid]:
      return arr[mid]
      
    elif x > arr[mid]:
      low = mid+1
      
    elif x < arr[mid]:
      high = mid-1
      
print(binary([1,2,3,4,5],3,0,len([1,2,3,4,5])-1))