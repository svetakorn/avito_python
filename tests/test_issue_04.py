from one_hot_encoder import fit_transform
import pytest


@pytest.mark.parametrize('input_list, expected', [
    (['banana', 'apple', 'banana', 'banana', 'orange'],
     [
         ('banana', [0, 0, 1]),
         ('apple', [0, 1, 0]),
         ('banana', [0, 0, 1]),
         ('banana', [0, 0, 1]),
         ('orange', [1, 0, 0])
     ]
     ),
    ({}, []),
    ((), []),
    ('one element', [('one element', [1])])
])
def test_full_output(input_list, expected):
    assert fit_transform(input_list) == expected


@pytest.mark.xfail(raises=TypeError)
def test_type_error():
    fit_transform(123)


@pytest.mark.xfail(raises=TypeError)
def test_no_arguments():
    fit_transform()


def test_max_binary_value():
    test_list = ['banana', 'apple', 'banana', 'banana', 'orange']
    output = fit_transform(test_list)
    assert max([i for l in output for i in l[1]]) == 1
