def inputElements(array):
  n = int(input("Enter the number of elements you want to sort : "))

  for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)

def heapify(array, size, i):
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2

  if left < size and array[left] > array[largest]:
    largest = left

  if right < size and array[right] > array[largest]:
    largest = right

  if largest != i:
    array[i], array[largest] = array[largest], array[i]

    heapify(array, size, largest)

def heapSort(array):
  size = len(array)
  for i in range(size // 2 - 1, -1, -1):
    heapify(array, size, i)
  
  for i in range(size - 1, 0, -1):
    array[0], array[i] = array[i], array[0]
    heapify(array, i, 0)

def printElements(array):
  for element in array:
    print(element)

def main():
  array = []

  inputElements(array)
  heapSort(array)
  printElements(array)

main()