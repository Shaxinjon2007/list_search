def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    
    i=0
    a=data[0]
    b=0
    while i<len(data):
        if a>data[i]:
            a=data[i]
            b=data.count(a)
        i=i+1
    return b
print(find_min_count([7,3,3,3,8,9,70,3,3,5,6,3,3]))
