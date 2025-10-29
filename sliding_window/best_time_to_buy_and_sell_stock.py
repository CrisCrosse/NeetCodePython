from turtledemo.paint import changecolor
from typing import List


class BruteForce:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_on_any_day = 0
        for i in range(len(prices)-1):
            price_today = prices[i]
            highest_price_seen_subsequently = 0

            for j in range(i+1, len(prices)):
                price_in_future = prices[j]
                if price_in_future > price_today and price_in_future > highest_price_seen_subsequently:
                    highest_price_seen_subsequently = price_in_future

            max_profit_for_ith_day = highest_price_seen_subsequently - price_today
            if max_profit_for_ith_day > max_profit_on_any_day:
                max_profit_on_any_day = max_profit_for_ith_day

        return max_profit_on_any_day

class Optimised:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price_seen_so_far = prices[0]
        highest_price_since_low = prices[0]
        for price in prices[1:]:
            print(f"today's price: {price}")
            if highest_price_since_low < price:
                highest_price_since_low = price
            elif price < lowest_price_seen_so_far:
                lowest_price_seen_so_far = price
                highest_price_since_low = price
            print(f"highest_price_since_low: {highest_price_since_low}, lowest_price_since_low: {lowest_price_seen_so_far}")
            current_profit = highest_price_since_low - lowest_price_seen_so_far
            print(f"current_profit: {current_profit}")
            if current_profit > max_profit:
                max_profit = current_profit
                print(f"max_profit: {max_profit}")

        return max_profit
