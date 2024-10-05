from option1 import findDuplicate1, findDuplicate2

"""
It is stated that the input contains exactly N+1 numbers and that each element
is present at least once in the domain [1, N]. From this, one can expect 
a single case of input where there is only one duplicate and not multiple ones.
Thus, all tests assume that the input contains one single duplicate.
"""

def test_duplicate_only() -> None:
    assert findDuplicate1([1, 1]) == 1
    assert findDuplicate2([1, 1]) == 1

def test_duplicate_at_the_end() -> None:
    assert findDuplicate1([4, 5, 3, 1, 2, 2]) == 2
    assert findDuplicate2([4, 5, 3, 1, 2, 2]) == 2

def test_duplicate_at_the_start() -> None:
    assert findDuplicate1([3, 3, 5, 4, 1, 2]) == 3
    assert findDuplicate2([3, 3, 5, 4, 1, 2]) == 3

def test_duplicate_dispersed() -> None:
    assert findDuplicate1([2, 4, 5, 3, 2, 1]) == 2
    assert findDuplicate2([2, 4, 5, 3, 2, 1]) == 2