def mode(list_in):
    """
    Calculate the mode

    :param list_in: A list
    :return: float
    """
    value = []
    count = []
    for val in list_in:
        if val in value:
             ind = value.index(val)
             count[ind] += 1
        else:
            value.append(val)
            count.append(1)
    v = max(count)
    max_ind = count.index(v)
    return float(value[max_ind])

