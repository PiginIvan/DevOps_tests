import pytest
from src.main import sum_of_digits, fibonacci


@pytest.mark.parametrize(
    ('n', 'ans'), [
        (3, 2),
        (6, 8),
        (10, 55),
    ]
)
def test_function_fibonacci(n, ans):
    assert fibonacci(n) == ans


@pytest.mark.parametrize(
    ('num', 'sum'), [
        (1157, 14),
        (33, 6),
        (100, 1),
    ]
)
def test_function_sum_of_digits(num, sum):
    assert sum_of_digits(num) == sum
