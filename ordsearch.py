def linear(data, value):
    """Return index of 'value' in list 'data', or -1 if it does not occur"""
    # Go through the data list from index 0 upwards
    i = 0
    # continue until value found or index outside valid range
    while i < len(data) and data[i] != value and data[i] < value:
        # increase the index to go to the next data value
        i = i + 1
    # test if we have found the value


    if i == len(data) :
        # no, we went outside valid range; return -1
        return -1

    elif data[i] > value:
        return -1

    else:
        # yes, we found the value; return the index
        return i


def linearPairs(data, value):

    i = 0
    while i < len(data) and data[i][0] != value:
        i = i + 1

    if i == len(data) :
        return -1
    else:
        return i

def binary(data,value):

    high = len(data)-1
    low = 0

    while low <= high and data[low] != value: #low <= high
        middle = (high + low)//2

        if(data[middle] == value):
            low = middle
        elif data[middle] < value:
            low = middle +1
        else:
            high = middle -1

    if high > low: #low > high => niet gevonden, anders zit ie op low
        return low
    else:
        return -1

def binary_pairs(data, value):
    if len(data) == 0:
        return -1

    high = len(data)-1
    low = 0

    while low <= high and data[low][0] != value:
        middle = int((high + low)/2)

        if data[middle][0] == value:
            low = middle
        elif data[middle][0] < value:
            low = middle + 1
        else:
            high = middle - 1

    if high > low:
        return low
    else:
        return -1





