import sys
sys.path.append('.')
sys.path.append('..')

from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(4) == 4
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(6) == 'fizz'
    assert fizzbuzz(7) == 'github'
    assert fizzbuzz(8) == 8
    assert fizzbuzz(9) == 'fizz'
    assert fizzbuzz(10) == 'buzz'
