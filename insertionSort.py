def inputElements(array, n):
  for i in range(n):
    element = int(input(f"Input element {i+1}: "))
    array.append(element)

def printResult(array):
  for element in (array):
    print(f"{element}")

def insertionSort(array, n):
  for i in range(1, n):
    temp = array[i]
    j = i - 1

    while j>=0 and array[j] > temp:
      array[j+1] = array[j]
      j -= 1

    array[j+1] = temp
    

def main():
  n = int(input("Enter the number of elements you want to sort: "))

  array = [] * n

  inputElements(array, n)
  insertionSort(array, n)
  printResult(array)

main()