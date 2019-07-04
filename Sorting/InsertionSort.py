import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

arr = []
for i in range(10):
    arr.append(random.randint(1, 100))

print("Unsorted: ")
print(arr)
print("Insertion Sorted: ")

small = False

for i in range(1, len(arr)):
    for j in range(i-1, 0, -1):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        
print(arr)