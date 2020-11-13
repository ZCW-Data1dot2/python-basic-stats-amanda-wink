from math import sqrt
from statzcw import zvariance

def st_dev(list_in):
    """
    Calculates the standard deviation. Square root of the variance.

    :param list_in: A list
    :return: A float
    """
    var = zvariance.variance(list_in)
    return float(sqrt(var))
