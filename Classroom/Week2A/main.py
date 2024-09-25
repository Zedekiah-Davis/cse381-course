# CSE 381 REPL 2A
# Binary Search

def search(data, target):
    first = 0
    last = len(data) - 1
    while first <= last:
        middle = (first + last) // 2
        if data[middle] == target:
            return middle
        if data[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    return -1

print(search([1,2,3,4,5,6],4))
print(search([1,2,3,4,5,6],0))