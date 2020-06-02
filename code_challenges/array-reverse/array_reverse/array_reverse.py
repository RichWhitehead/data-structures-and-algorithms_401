def __reverseArray__(arr):
  reverseArr = []
  for i in range(0, len(arr)):
    reverseArr.append(arr[len(arr) - i - 1])
  return reverseArr