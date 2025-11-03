from functools import cmp_to_key
from unittest import TestCase

class BankAccount:
    def __init__(self, account_id: str, total: int) -> None:
        self.account_id = account_id
        self.total_transaction_value = total


class BankingImplementation:
    def __init__(self):
        self.accounts = { "accountC": BankAccount(account_id="accountC", total=10),
                          "accountA": BankAccount(account_id="accountA", total=10),
                          "accountB": BankAccount(account_id="accountB", total=10),
                          "accountD": BankAccount(account_id="accountD", total=20),
                          "accountE": BankAccount(account_id="accountE", total=5),}


class TestSorting(TestCase):
    def test_customSort(self):
        bank = BankingImplementation()
        accounts = []
        for account in bank.accounts.values():
            accounts.append((account.account_id, account.total_transaction_value))
        accounts.sort(key=cmp_to_key(customSort))

        self.assertEqual(accounts,[
            ("accountD", 20),
            ("accountA", 10),
            ("accountB", 10),
            ("accountC", 10),
            ("accountE", 5)
        ])


def customSort(a, b):
    if a[1] < b[1]:
        return 1
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return -1
        else:
            return 1
    else:
        return -1