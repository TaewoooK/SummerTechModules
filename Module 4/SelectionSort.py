import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

arr = []
for i in range(10):
	arr.append(random.randint(1, 100))

print("Unsorted: ")
print(arr)
print("Selection Sorted: ")

for i in range(len(arr)):
    smallest = arr[i]
    sIndex = i
    change = False
    for j in range(i, len(arr)):
        if smallest > arr[j]:
            smallest = arr[j]
            sIndex = j
            change = True
    if change == True:
        temp = arr[i]
        arr[i] = smallest
        arr[sIndex] = temp
print(arr)
