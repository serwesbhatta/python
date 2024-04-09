def inputElements(array):
  n = int(input("Enter the number of elements you want to sort : "))

  for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)

def heapify(array, i):
  largest = i
  left = i * 2 + 1
  right = i * 2 + 2

  if left < len(array) and array[left] > array[largest]:
    largest = left

  if right < len(array) and array[right] > array[largest]:
    largest = right

  if largest != i:
    array[i], array[largest] = array[largest], array[i]

    heapify(array, largest)

def heapSort(array):
  for i in range(len(array) // 2 - 1, -1, -1):
    heapify(array, i)
  
  for i in range(len(array) - 1, 0, -1):
    array[0], array[i] = array[i], array[0]
    heapify(array, i)

def printElements(array):
  for element in array:
    print(element)

def main():
  array = []

  inputElements(array)
  heapSort(array)
  printElements(array)

main()