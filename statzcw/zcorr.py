import statzcw
from statzcw import zcount
from statzcw import zmean
from statzcw import zstddev

def correlation(listx, listy):
    num = 0
    sample = zcount.count(listx)
    x_mean = zmean.mean(listx)
    y_mean = zmean.mean(listy)
    s_x = zstddev.st_dev(listx)
    s_y = zstddev.st_dev(listy)
    for i in range(len(listx)):
        x_diff = float(listx[i]) - x_mean
        y_diff = float(listy[i]) - y_mean
        num += x_diff * y_diff
    return ((num / (s_x * s_y))/ (sample - 1))
