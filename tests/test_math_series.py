from math_series import __version__
from math_series.math_series import  recur_fibo , recur_lucas, sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_zero():
    expected = 0
    actual = recur_fibo(0)
    assert expected == actual

def test_one():
    expected = 1
    actual = recur_fibo(1)
    assert expected == actual

def test_ten():
    expected = 55
    actual = recur_fibo(10)
    assert expected == actual

def test_thirteen():
    expected = 233
    actual = recur_fibo(13)
    assert expected == actual

def test_twenty_three():
    expected = 28657
    actual = recur_fibo(23)
    assert expected == actual

# ******** Lucas ***********

def test_zero_lucas():
    expected = 2
    actual = recur_lucas(0)
    assert expected == actual

def test_one_lucas():
    expected = 1
    actual = recur_lucas(1)
    assert expected == actual

def test_ten_lucas():
    expected = 123
    actual = recur_lucas(10)
    assert expected == actual

def test_thirteen_lucas():
    expected = 521
    actual = recur_lucas(13)
    assert expected == actual


def test_twenty_three_lucas():
    expected = 64079
    actual = recur_lucas(23)
    assert expected == actual

    # ***** sum_series ******

def test_sum_zeros():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_tows():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_three():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_ten():
    actual = sum_series(10,2,1)
    expected = 123
    assert actual == expected

def test_sum_twenty_5_5():
    actual = sum_series(20,5,5)
    expected = 6776
    assert actual == expected

def test_sum_thirteen_10_6():
    actual = sum_series(13,10,6)
    expected = 356
    assert actual == expected

def test_sum_twenty_three_5_3():
    actual = sum_series(23,5,3)
    expected = 28668
    assert actual == expected

def test_sum_fifteen_4_3():
    actual = sum_series(15,4,3)
    expected = 617
    assert actual == expected