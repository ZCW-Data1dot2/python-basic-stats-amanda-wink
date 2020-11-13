from statzcw import zcount
from statzcw import zcorr
from statzcw import zmean
from statzcw import zmedian
from statzcw import zmode
from statzcw import zstddev
from statzcw import zstderr
from statzcw import zvariance
from csv import reader

def read_csv(file):
    with open(file, 'r') as f:
        csv_reader = reader(f)
        list_in = list(csv_reader)
        return list_in

def list_break(list_in):
    x_list1 = []
    y_list1 = []
    for i in range(len(list_in)):
        x_list1.append(list_in[i][0])
        y_list1.append(list_in[i][1])
    return x_list1, y_list1


def main(file_list):
    for file_num in file_list:
        print(file_num)
        work_list = read_csv(file_num)
        x_list, y_list = list_break(work_list)
        x_list.pop(0)
        y_list.pop(0)

        x_count = zcount.count(x_list)
        y_count = zcount.count(y_list)
        x_mean = round(zmean.mean(x_list), 3)
        x_var = round(zvariance.variance(x_list), 3)
        y_mean = round(zmean.mean(y_list), 3)
        y_var = round(zvariance.variance(y_list), 3)
        corr = round(zcorr.correlation(x_list, y_list), 3)
        x_median = round(zmedian.median(x_list), 3)
        y_median = round(zmedian.median(y_list), 3)
        x_mode = zmode.mode(x_list)
        y_mode = zmode.mode(y_list)
        x_stdev = round(zstddev.st_dev(x_list), 3)
        y_stdev = round(zstddev.st_dev(y_list), 3)
        x_sterr = round(zstderr.st_err(x_list), 3)
        y_sterr = round(zstderr.st_err(y_list), 3)
        print("Simple: "  + str(x_mean) + " " + str(x_var) + " " +
              str(y_mean) + " " + str(y_var) + " " + str(corr))
        print("Complex x: " + str(x_median) + " " + str(x_mode) + " " +
              str(x_stdev) + " " + str(x_sterr))
        print("Complex y: " + str(y_median) + " " + str(y_mode) + " " +
              str(y_stdev) + " " + str(y_sterr))


if __name__ == '__main__':
    file_list1 = ['/Users/amanda/Documents/PythonProjects/python-basic-stats-amanda-wink/dataZero.csv',
                '/Users/amanda/Documents/PythonProjects/python-basic-stats-amanda-wink/dataOne.csv',
                '/Users/amanda/Documents/PythonProjects/python-basic-stats-amanda-wink/dataTwo.csv',
                '/Users/amanda/Documents/PythonProjects/python-basic-stats-amanda-wink/dataThree.csv'
                ]
    main(file_list1)