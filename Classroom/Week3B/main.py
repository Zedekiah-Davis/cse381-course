# CSE 381 REPL3B 
# Merge Sort

def Sort(data):
    _Sort(data, 0, len(data)-1)

def _Sort(data, first, last):
    if first >= last:
        # first > last means empty
        #first = last means size 1
        return
    mid = (first + last) // 2
    _Sort(data, first, mid)
    _Sort(data, mid + 1, last)
    Merge(data, first, mid, last)

def Merge(data, first, mid, last):
    sa1 = data[first:mid+1]
    sa2 = data[mid+1:last+1]
    sa1Index = 0
    sa2Index = 0

    for index in range(first, last+1):
        if sa1Index >= len(sa1):
            data[index] = sa2[sa2Index]
            sa2Index += 1
        elif sa2Index >= len(sa2):
            data[index] = sa1[sa1Index]
            sa1Index += 1
        elif sa1[sa1Index] <= sa2[sa2Index]:
            data[index] = sa1[sa1Index]
            sa1Index =+ 1
        else:
            data[index] = sa2[sa2Index]
            sa2Index =+ 1

data = [3,1,2,6,4,5]
Sort(data)
print(data)