import os

os.system('cls' if os.name == 'nt' else 'clear')
arr = []
arr.append(2)
arr.append(4)
arr.append(7)
arr.append(10)
arr.append(12)
arr.append(13)
arr.append(14)

def search(left, right, mid, find):
    mid = left+right
    mid = int(mid/2)
    if arr[mid] == find:
        return mid
    else:
        if arr[mid] > find:
            return search(left, mid-1, right, find)
        elif arr[mid] < find:
            return search(mid+1, right, left, find)

print(arr)
searchNum = int(input("Which number would you like to find the index of? "))

found = 0
for i in range(len(arr)):
    if arr[i] == searchNum:
        found += 1
if found == 0:
    print("Number is not in array!")
else:
    print(search(0, len(arr)-1, 0, searchNum))



