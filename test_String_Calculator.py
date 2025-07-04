###     This is testStringCalculator.py     ###

from string_Calculator import StringCalculator

def test_empty_string_return_zero():
    sc = StringCalculator()
    assert sc.Add("")==0