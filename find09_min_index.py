def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    i=0
    a=data[0]
    k=0
    while i<len(data):
        if a>data[i]:
           a=data[i] 
           k=data.index(a)
        i=i+1
    return k
print(find_min_index([1,2,-3,4,5]))


