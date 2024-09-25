# CSE 381 REPL 2B 
# Recursive Binary Search

def _search(data, target, first, last):
    if first > last:
        return -1
    middle = (first + last) // 2
    if data[middle] == target:
        return middle
    if data[middle] > target:
        return _search(data, target, first, middle -1)
    else:
        return _search(data, target, middle + 1, last)
    
def search(data, target):
    return _search(data, target, 0, len(data) - 1)

print(search([1,2,3,4,5,6],4))
print(search([1,2,3,4,5,6],0))