def linear(data, value):
    """Return index of 'value' in list 'data', or -1 if it does not occur"""
    # Go through the data list from index 0 upwards
    i = 0
    # continue until value found or index outside valid range
    while i < len(data) and data[i] != value:
        # increase the index to go to the next data value
        i = i + 1
    # test if we have found the value
    if i == len(data):
        # no, we went outside valid range; return -1
        return "Komt niet voor"
    else:
        # yes, we found the value; return the index
        return i
