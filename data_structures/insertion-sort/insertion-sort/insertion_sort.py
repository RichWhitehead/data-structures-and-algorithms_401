


def insertion_sort(arr):
    for i in range (1, len(arr)):
      key = arr [i]
      j = i-1
      while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
        arr[j+1] = key

# Driver code to test above
arr = [8,4,23,42,16,15]
insertion_sort(arr)
print('sorted array is:')
for i in range(len(arr)):
  print (arr[i])
