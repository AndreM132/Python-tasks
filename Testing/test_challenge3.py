import pytest
from Code import challenge3

def test_d():
    assert challenge3.dicgen(2) == {1:1, 2:4}