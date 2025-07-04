###     This is testStringCalculator.py     ###

from string_Calculator import StringCalculator

def test_empty_string_return_zero():
    sc = StringCalculator()
    assert sc.Add("")==0

def test_single_number_return_itself():
    sc = StringCalculator()
    assert sc.Add("1")==1

def test_two_numbers_return_sum():
    sc = StringCalculator()
    assert sc.Add("1,2")==3

def test_unknown_amount_numbers_return_sum():
    sc = StringCalculator()
    assert sc.Add("1,2,3")==6
    assert sc.Add("3,4,5,6,7")==25

### Defining test case through \n ###
def test_newline_delimeter_sum():
    sc = StringCalculator()
    assert sc.Add("1\n2,3")==6
    assert sc.Add("1\n4")==5