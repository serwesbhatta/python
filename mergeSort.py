def inputElements(array):
  n = int(input("Enter the number of elements you want to sort: "))

  for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)


def merge(left, right, array):
  i = j = k = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      array[k] = left[i]
      i += 1
    else:
      array[k] = right[j]
      j += 1
    k += 1

  while i < len(left):
    array[k] = left[i]
    i += 1
    k += 1
  
  while j < len(right):
    array[k] = right[j]
    j += 1
    k += 1

def mergeSort(array):
  if len(array) >= 2:
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    mergeSort(left)
    mergeSort(right)

    merge(left, right, array)


def printResult(array):
  print("The elements are sorted in the following way: ")
  for element in array:
    print(element)


def main():
  array = []

  inputElements(array)
  mergeSort(array)
  printResult(array)

main()