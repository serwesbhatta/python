# Function to take input for the array from the user
def inputElements(array, n):
  for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)

def printResult(array):
  for element in array:
    print(f"{element}")

# Function that implements bubble sort algorithm
def selectionSort(array, n):
  for i in range(n-1):
    minIndex = i;
    for j in range(i+1, n):
      if(array[j] < array[minIndex]):
        minIndex = j
    
    if minIndex  != i:
      array[i], array[minIndex] = array[minIndex], array[i]

def main():
  n = int(input("Enter number of elements you want to sort: "))

  array = [] * n

  inputElements(array, n)
  selectionSort(array, n)
  printResult(array)

main()