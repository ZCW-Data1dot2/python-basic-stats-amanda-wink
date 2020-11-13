def median(list_in):
    """
    Calculates the median of the data

    :param list_in: A list
    :return: float
    """
    list_in.sort()
    half = int(len(list_in) / 2)
    if len(list_in) % 2 != 0:
        return float(list_in[half])
    elif len(list_in) % 2 ==0:
        value = (list_in[half - 1] + list_in[half]) / 2
        return float(value)

#list_inp = [6,9,4,5,2,1,7,3,0,7,3, 14, 2, 7, 18, 23, 1, 12, 9]
#print(median(list_inp))