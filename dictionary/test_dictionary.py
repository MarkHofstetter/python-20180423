import pytest
from dictionary import translate


def test_answer():
    testdict = {
        'a': 'b',
        'c': 'd',
    }

    assert translate('a', testdict) == 'b'
    assert translate('b', testdict) == 'a'


def test_answer2():
    testdict = {
        'a': 'b',
        'c': 'd',
    }

    assert translate('a', testdict) == 'b'
    assert translate('b', testdict) == 'a'


def test_not_found():
    testdict = {}
    with pytest.raises(ValueError):
        assert translate('f', testdict) == 'b'
