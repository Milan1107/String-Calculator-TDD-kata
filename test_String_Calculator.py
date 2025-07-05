###     This is test_String_Calculator.py     ###

from string_Calculator import StringCalculator
import pytest

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

### allowing different delimeters as input
def test_different_delimeters_sum():
    sc = StringCalculator()
    assert sc.Add("//;\n1;2")==3    # here delimeter is ;

### avoidning single negative number
def test_negative_number_throw_exception():
    sc = StringCalculator()
    with pytest.raises(ValueError,match="negative numbers are not allowed:-5"):
        sc.Add("3,-5,6")

### defining a test case for public int GetCalledCount()
def test_add_called_count():
    sc = StringCalculator()
    assert sc.GetCalledCount()==0

    sc.Add("2,5")
    sc.Add("1\n100")

    assert sc.GetCalledCount()==2

### number shouldn't be greater than 1000
def test_number_not_exceed_one_thousand():
    sc = StringCalculator()
    assert sc.Add("2,1000")==1002
    assert sc.Add("2,1001")==2

### delimeter can be of any lenght
def test_any_length_delimeter():
    sc = StringCalculator()
    assert sc.Add("//[***]\n1***2***3")==6