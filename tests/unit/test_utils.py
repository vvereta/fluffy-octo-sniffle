import math

from fluffy import utils

import pytest


@pytest.mark.parametrize('numbers', [(1, 2), (3, 4), (-1, -2)])
def test_add(numbers):
    assert utils.add(*numbers) == sum(numbers)


def test_get_pi():
    math.pi = 3.14
    assert utils.get_pi() == 3.14
