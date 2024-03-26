# Function to take input for the array from the user
def inputElements():
  array = []
  n = int(input("Enter number of elements you want to sort: "))

  for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)
  
  return array

def printResult(array):
  for element in array:
    print(f"{element}")

# Function that implements bubble sort algorithm
def buubleSort(array):
  swapped = True
  j = 0
  while(swapped):
    swapped = False
    j += 1
    for i in range(len(array) - j):
      if(array[i] > array[i+1]):
        array[i], array[i+1] = array[i+1], array[i]
        swapped = True
        i = 0

def main():
  array = inputElements()
  buubleSort(array)
  printResult(array)

main()