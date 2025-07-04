from string_Calculator import StringCalculator

sc = StringCalculator()
print("Input \" \" : ",sc.Add(""))
print("Input \"7\" : ",sc.Add("7"))
print("Input \"4,5\" : ",sc.Add("4,5"))
print("Input \"3,4,5,6,7\" : ",sc.Add("3,4,5,6,7"))
#   added new line with , #
print("Input \"6,90\\n100\" : ",sc.Add("6,90\n100"))
#   different types of delimeter can be used
print("Input \"//;\\n10;200\" : ",sc.Add("//-\n10-200"))
#   signle/multiple negative number is handled

try:
    print("Input \"3,-100,-7\" : ", sc.Add("3,-100,-7"))
except ValueError as e:
    print("Exception caught:", e)
#   printing GetCalledCount()'s value
print("Called Count for Add() is : ",sc.GetCalledCount())
#   Number greater than 1000 is avoided
print("Input \"10,2000\" : ",sc.Add("10,2000"))
#   Multiple delimeter can be allowed
print("Input \"//[***]\\n1***2***3\" : ", sc.Add("//[***]\n1***2***3"))
#   Multiple different delimeter can be allowed
print("Input \"//[*][%]\\n1*2%3\" : ", sc.Add("//[*][%]\n1*2%3"))
