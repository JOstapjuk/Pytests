import pytest
from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

# C-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_bankaccount_init_and_balance():
    acc = BankAccount("Alice", 100)
    assert acc.balance() == 100

    acc2 = BankAccount("Bob")
    assert acc2.balance() == 0

    BankAccount("Alice", 0)
    BankAccount("Owner", 50)


def test_bankaccount_deposit_and_withdraw():
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    assert acc.balance() == 150

    acc.withdraw(30)
    assert acc.balance() == 120


def test_bankaccount_transfer():
    a = BankAccount("Alice", 100)
    b = BankAccount("Bob", 50)
    a.transfer_to(b, 40)
    assert a.balance() == 60
    assert b.balance() == 90

def test_fibonacci_small():
    assert [fibonacci(i) for i in range(6)] == [0, 1, 1, 2, 3, 5]
    assert fibonacci(10) == 55


def test_prime_factors_basic():
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(97) == [97]
    assert prime_factors(100) == [2, 2, 5, 5]

def test_moving_average_basic():
    values = [1, 2, 3, 4, 5]
    assert moving_average(values, 1) == [1, 2, 3, 4, 5]
    assert moving_average(values, 2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average(values, 3) == [2.0, 3.0, 4.0]
    assert moving_average(values, 10) == []

def test_normalize_scores_basic():
    assert normalize_scores([0, 50, 100]) == [0.0, 0.5, 1.0]
    assert normalize_scores([20, 80]) == [0.2, 0.8]

# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
