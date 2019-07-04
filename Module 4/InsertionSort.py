import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

arr = []
for i in range(10):
	arr.append(random.randint(1, 100))

print("Unsorted: ")
print(arr)
print("Insertion Sorted: ")

for i in range(1, len(arr)):
	current = arr[i]
	j = i-1
	while j>=0 and current < arr[j]:
		arr[j+1] = arr[j]
		j -= 1
	arr[j+1] = current
		
print(arr)