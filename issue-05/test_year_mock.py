from what_is_year_now import what_is_year_now
from unittest.mock import patch
import pytest
import urllib.request
import io


def test_year():
    exp_year = 2021
    prev_year = 2020
    date = """{"currentDateTime": "2021-12-02"}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(date)):
        year = what_is_year_now()
    assert year == exp_year
    assert year != prev_year


def test_year_another_format():
    exp_year = 2021
    prev_year = 2020
    date = """{"currentDateTime": "02.12.2021"}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(date)):
        year = what_is_year_now()
    assert year == exp_year
    assert year != prev_year


def test_year_wrong_format():
    date = """{"currentDateTime": "02/12/2021"}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(date)):
        with pytest.raises(ValueError):
            what_is_year_now()

