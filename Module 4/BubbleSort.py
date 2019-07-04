import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

arr = []

for i in range(10):
    arr.append(random.randint(1, 100))
print("Unsorted: ")
print(arr)
print("Bubble Sorted: ")

for j in range(len(arr)):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

print(arr)