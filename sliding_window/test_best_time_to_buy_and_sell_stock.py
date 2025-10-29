from unittest import TestCase

from sliding_window.best_time_to_buy_and_sell_stock import BruteForce, Optimised


class TestBruteForce(TestCase):
    def test_max_profit(self):
        profit = BruteForce().maxProfit([10,1,5,6,7,1])
        self.assertEqual(profit, 6)

class TestOptimised(TestCase):
    def test_max_profit(self):
        profit = Optimised().maxProfit([10,1,5,6,7,1])
        self.assertEqual(profit, 6)

    def test_max_profit_only_one_day(self):
        profit = Optimised().maxProfit([10])
        self.assertEqual(profit, 0)
