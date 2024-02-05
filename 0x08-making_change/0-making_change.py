#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    coin_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while total > 0:
        if coin_idx >= n:
            return -1
        if total - sorted_coins[coin_idx] >= 0:
            total -= sorted_coins[coin_idx]
            coin_count += 1
        else:
            coin_idx += 1
    return coin_count
