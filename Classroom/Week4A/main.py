# CSE 381 REPL4A 
# Quick Sort

def Sort(data):
    _Sort(data, 0, len(data) - 1)

def _Sort(data, first, last):
    if (first >= last):
        return
    pivotIndex = Partition(data, first, last)
    _Sort(data, first, pivotIndex - 1)
    _Sort(data, pivotIndex + 1, last)


def Partition(data, first, last):
    pivot = (first + last) // 2
    data[pivot], data[last] = data[last], data[pivot]

    leftMostGreaterPivot = first
    for index in range(first, last):
        if data[index] <= data[last]:
            data[leftMostGreaterPivot], data[index] = data[index], data[leftMostGreaterPivot]
            leftMostGreaterPivot += 1

    data[leftMostGreaterPivot], data[last] = data[last], data[leftMostGreaterPivot]
    return leftMostGreaterPivot


data = [6,1,3,7,2,5,8,4]
Sort(data)
print(data)