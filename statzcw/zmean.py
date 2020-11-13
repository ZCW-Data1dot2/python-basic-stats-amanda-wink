from statzcw import zcount

def mean(list_in):
    """
    Calculates the mean of a given list

    :param list_in: A list
    :return:
    """
    total = sum([float(t) for t in list_in])
    mean_value = total / zcount.count(list_in)
    return float(mean_value)



if __name__ == "main":
    list_in = [9, 7, 18, 6]
    mean(list_in)