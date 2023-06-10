def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i=0
    y=data[0]
    while i<len(data):
        if data[i]%2==0 and y>data[i]:
            y=data[i]
        i=i+1
    return y
print(find_min_even([1,8,2,8,5]))

