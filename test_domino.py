import pytest
from domino import *


def test_flip():
    res = flip("/", 'prev')
    assert res == ("/", True)


def test_value_error():
    with pytest.raises(ValueError):
        domino_falling("//|", "forward", -1)


def test_iterate_forward():
    result = domino_falling(
        r"//||\\\|", "forward", 2
    )

    expected = [
       r"///\\\\|", r"///\\\\|"
    ]

    assert result == expected


def test_iterate_reverse():
    result = domino_falling(
        r"////|\\||", "reverse", 2
    )

    expected = [
        r"///|||\||", r"//|||||||"
    ]
