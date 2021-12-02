import pytest
from letterToMorse import decode


@pytest.mark.parametrize('message, expected', [
    ('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019'),
    ('... --- ...', 'SOS')
])
def test_decode(message, expected):
    assert decode(message) == expected


def test_exception():
    with pytest.raises(KeyError):
        decode('Check for key error')

