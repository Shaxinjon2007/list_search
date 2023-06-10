def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i=0
    m=0
    while i<len(data):
        if data [i]%2==1:
            m=data[i]
        i=i+1
    return m
print(find_max_odd([1,3,2,13,7,79,14,28]))
