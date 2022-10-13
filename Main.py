from typing import List

def selectionSort(array, size) -> List[int]:
  for s in range(size):
    min = step
    for i in range(s + 1, size):
      if array[i] < array[min]:
        min = i
    (array[s], array[min]) = (array[min], array[s])
  return array

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
