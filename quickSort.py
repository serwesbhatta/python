def inputElements(array, n):
  for i in range(n):
    element = int(input(f"Input element {i+1}: "))
    array.append(element)

def printResult(array):
  for element in (array):
    print(f"{element}")

def partition(array, b, e):
  p = b

  while b < e:
    while b < e and array[b] <= array[e]:
      e -= 1
    
    if array[b] > array[e]:
      array[b], array[e] = array[e], array[b]
      p = e
      b +=1
    
    while b < e and array[b] <= array[e]:
      b += 1
    
    if array[b] > array[e]:
      array[b], array[e] = array[e], array[b]
      p = b
      e -= 1
  
  return p

def quickSort(array, p, r):
  if p < r:
    q = partition(array, p, r)
    quickSort(array, p, q-1)
    quickSort(array,q+1, r)    

def main():
  n = int(input("Enter the number of elements you want to sort: "))

  array = []

  inputElements(array, n)
  quickSort(array, 0, n-1)
  printResult(array)

main()