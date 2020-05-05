from morse import decode
import pytest


@pytest.mark.parametrize('morse_string, expected', [
    ('... --- ...', 'SOS'),
    ('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019'),
    ('', ''),
    (' ', '')
])
def test_decode(morse_string, expected):
    assert decode(morse_string) == expected
