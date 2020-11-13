from math import sqrt
from statzcw import zstddev
from statzcw import zcount

def st_err(list_in):
    """
    Calculates the standard deviation error. Standard deviation divided by the sqrt of the count.
    :param list_in:
    :return:
    """
    stdev = zstddev.st_dev(list_in)
    denom = sqrt(zcount.count(list_in))
    return float(stdev / denom)