def inputElements(array):
  n = int(input("Enter the number of elements you want to sort : "))

  for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)

def printElements(array):
  for element in array:
    print(element)

