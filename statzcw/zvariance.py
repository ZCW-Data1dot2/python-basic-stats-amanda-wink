from statzcw import zmean
from statzcw import zcount

def variance(list_in):
    """
    Calculates the variance.

    :param list_in: A list
    :return: A float
    """
    var_top = 0
    data_mean = zmean.mean(list_in)
    for val in list_in:
        diff = float(val) - data_mean
        sq_diff = diff ** 2
        var_top += sq_diff
    count_val = zcount.count(list_in) - 1
    var = var_top / count_val
    return float(var)