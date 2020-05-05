from morse import encode, LETTER_TO_MORSE
import doctest


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('MAI-PYTHON-2019') # doctest: +ELLIPSIS
    '-- .- .. ... .---- ----.'
    >>> encode(3.14) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    TypeError: input must be string
    >>> encode('строка для exception') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    KeyError: 'с'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == "__main__":
    doctest.testmod()
