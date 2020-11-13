import unittest
from statistics import stdev
from statistics import variance
from scipy.stats import sem
from scipy.stats import pearsonr
from statzcw import zcount
from statzcw import zmean
from statzcw import zmedian
from statzcw import zmode
from statzcw import zvariance
from statzcw import zstddev
from statzcw import zstderr
from statzcw import zcorr


class Test_Stat(unittest.TestCase):

    def test_count(self):
        test_cases = [
            ([5, 9, 14, 7], 4),
            ([12, 17, 2, 8, 31, 9, 5], 7),
            ([29, 14, 5, 29, 15, 18, 8, 22, 6, 11], 10),
            ([42.53, 17.2, 7.87, 24.12, 13.63], 5),
        ]

        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zcount.count(list_in))

    def test_mean(self):
        test_cases = [
            ([5, 9, 14, 7], 8.75),
            ([12, 17, 2, 8, 31, 9, 5], 12),
            ([29, 14, 5, 29, 15, 18, 8, 22, 6, 11], 15.7),
            ([42.53, 17.2, 7.87, 24.12, 13.63], 21.07),
        ]

        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zmean.mean(list_in))

    def test_median(self):
        test_cases = [
            ([5, 9, 14, 7], 8),
            ([12, 17, 2, 8, 31, 9, 5], 9),
            ([29, 14, 5, 29, 15, 18, 8, 22, 6, 11], 14.5),
            ([42.53, 17.2, 7.87, 24.12, 13.63], 17.2),
        ]

        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zmedian.median(list_in))

    def test_mode(self):
        test_cases = [
            ([5, 9, 14, 7, 9], 9),
            ([2, 12, 17, 2, 8, 31, 9, 5], 2),
            ([29, 14, 5, 29, 15, 11, 18, 8, 22, 6, 29, 11], 29),
            ([42.53, 42.53, 17.2, 7.87, 24.12, 13.63], 42.53),
            ([29, 14, 11, 5, 29, 15, 11, 18, 8, 22, 6, 29, 11], 29)
        ]

        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertEqual(expected, zmode.mode(list_in))

    def test_variance(self):
        test_cases = [
            ([5, 9, 14, 7], variance([5, 9, 14, 7])),
            ([12, 17, 2, 8, 31, 9, 5], variance([12, 17, 2, 8, 31, 9, 5])),
            ([29, 14, 5, 29, 15, 18, 8, 22, 6, 11],variance([29, 14, 5, 29, 15, 18, 8, 22, 6, 11])),
            ([42.53, 17.2, 7.87, 24.12, 13.63], variance([42.53, 17.2, 7.87, 24.12, 13.63])),
        ]

        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertAlmostEqual(expected, zvariance.variance(list_in))


    def test_st_dev(self):
        test_cases = [
            ([5, 9, 14, 7], stdev([5, 9, 14, 7])),
            ([12, 17, 2, 8, 31, 9, 5], stdev([12, 17, 2, 8, 31, 9, 5])),
            ([29, 14, 5, 29, 15, 18, 8, 22, 6, 11],stdev([29, 14, 5, 29, 15, 18, 8, 22, 6, 11])),
            ([42.53, 17.2, 7.87, 24.12, 13.63], stdev([42.53, 17.2, 7.87, 24.12, 13.63])),
        ]

        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertAlmostEqual(expected, zstddev.st_dev(list_in))

    def test_st_err(self):
        test_cases = [
            ([5, 9, 14, 7], sem([5, 9, 14, 7])),
            ([12, 17, 2, 8, 31, 9, 5], sem([12, 17, 2, 8, 31, 9, 5])),
            ([29, 14, 5, 29, 15, 18, 8, 22, 6, 11],sem([29, 14, 5, 29, 15, 18, 8, 22, 6, 11])),
            ([42.53, 17.2, 7.87, 24.12, 13.63], sem([42.53, 17.2, 7.87, 24.12, 13.63])),
        ]

        for list_in, expected in test_cases:
            with self.subTest(f"{list_in} -> {expected}"):
                self.assertAlmostEqual(expected, zstderr.st_err(list_in))

    def test_st_corr(self):
        test_cases = [
            ([5, 9, 14, 7],[23, 17, 2, 6], pearsonr([5, 9, 14, 7],[23, 17, 2, 6])),
            ([12, 17, 2, 8, 31, 9, 5], [4, 28, 19, 8, 12, 3, 12], pearsonr([12, 17, 2, 8, 31, 9, 5], [4, 28, 19, 8, 12, 3, 12]))
        ]

        for list_in_x, list_in_y, expected in test_cases:
            with self.subTest(f"{list_in_x, list_in_y} -> {expected}"):
                self.assertAlmostEqual(expected[0], zcorr.correlation(list_in_x, list_in_y))
