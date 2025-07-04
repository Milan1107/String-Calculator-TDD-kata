###     This is stringCalculator.py     ###

#   --- importing re for usage of reguler exp for ','|'\n' 
import re

class StringCalculator:
    def Add(self,numbers:str)->int:
        if numbers == "":
            return 0
        
        delimeter_pattern = r",|\n"

        if numbers.startswith("//"):
            parts = numbers.split("\n",1)
            delimeter = parts[0][2]
            numbers = parts[1]
            delimeter_pattern = re.escape(delimeter)
        
        tocken = re.split(delimeter_pattern,numbers)
        return sum(int(t) for t in tocken)