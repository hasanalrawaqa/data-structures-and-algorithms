from insertion import insertion_sort
import pytest

def test_insertion_sort_case1():
    arr = [8, 4, 23, 42, 16, 15]
    expected = [4, 8, 15, 16, 23, 42]
    insertion_sort(arr)
    assert arr == expected

def test_insertion_sort_case2():
    arr = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    insertion_sort(arr)
    assert arr == expected

def test_insertion_sort_case3():
    arr = [5, 12, 7, 5, 5, 7]
    expected = [5, 5, 5, 7, 7, 12]
    insertion_sort(arr)
    assert arr == expected

def test_insertion_sort_case4():
    arr = [2, 3, 5, 7, 13, 11]
    expected = [2, 3, 5, 7, 11, 13]
    insertion_sort(arr)
    assert arr == expected
