"""Units tests for the successive approximation."""
import unittest

from bisect.bisect import Bisect


class TestBisection(unittest.TestCase):
    """test class for bisection"""
    def test_too_big(self):
        dut = Bisect(0, 4)  # [0, 4] -> 2

        self.assertAlmostEqual(dut.Suggestion(), 2)
        dut.TooBig()  # [0, 2[ -> 1
        self.assertAlmostEqual(dut.Suggestion(), 1)
        dut.TooBig()  # [0, 1[ -> 0.5
        self.assertAlmostEqual(dut.Suggestion(), 0.5)

    def test_too_small(self):
        dut = Bisect(0, 4)  # [0, 4] -> 2

        self.assertAlmostEqual(dut.Suggestion(), 2)

        dut.TooSmall()  # ]2, 4] -> 3
        self.assertAlmostEqual(dut.Suggestion(), 3)
        dut.TooSmall()  # ]3, 4] -> 3.5
        self.assertAlmostEqual(dut.Suggestion(), 3.5)

    def test_small_big(self):
        dut = Bisect(0, 4)  # [0, 4] -> 2

        dut.TooSmall()  # -> ]2, 4] -> 3
        dut.TooBig()  # -> ]2, 3[ -> 2.5
        self.assertAlmostEqual(dut.Suggestion(), 2.5)

    def test_big_small(self):
        dut = Bisect(0, 4)  # [0, 4] -> 2

        dut.TooBig()  # -> ]0, 2[ -> 1
        dut.TooSmall()  # -> ]1, 2[ -> 1.5
        self.assertAlmostEqual(dut.Suggestion(), 1.5)

    def test_confuse_borders(self):
        dut = Bisect(lower=4, upper=1)
        self.assertAlmostEqual(dut.Suggestion(), 2.5)

    def test_find_borders_small_small_big(self):
        dut = Bisect(current=2)

        self.assertEqual(dut.Suggestion(), 2)

        dut.TooSmall()  # ]2, None[ -> 4
        self.assertAlmostEqual(dut.Suggestion(), 4)
        dut.TooSmall()  # ]4, None[ -> 8
        self.assertAlmostEqual(dut.Suggestion(), 8)
        dut.TooBig()  # ]4, 8[ -> 6
        self.assertAlmostEqual(dut.Suggestion(), 6)
        dut.TooSmall()  # ]6, 8[ -> 7
        self.assertAlmostEqual(dut.Suggestion(), 7)

    def test_find_borders_big(self):
        dut = Bisect(current=2)

        dut.TooBig()  # ]0, 2[ -> 1
        self.assertAlmostEqual(dut.Suggestion(), 1)
        dut.TooSmall()  # ]1, 2[ -> 1.5
        self.assertAlmostEqual(dut.Suggestion(), 1.5)

    def test_invalid_initialisation(self):
        with self.assertRaises(ValueError):
            _ = Bisect()

        with self.assertRaises(ValueError):
            _ = Bisect(current=None, lower=None, upper=1)

        with self.assertRaises(ValueError):
            _ = Bisect(current=None, lower=1, upper=None)

        with self.assertRaises(ValueError):
            _ = Bisect(current=1, lower=1, upper=None)

        with self.assertRaises(ValueError):
            _ = Bisect(current=1, lower=None, upper=1)

        with self.assertRaises(ValueError):
            _ = Bisect(lower=1, upper=1)


### test list
