###     This is string_Calculator.py     ###

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

        total = 0
        negatives = []

        for t in tocken:
            num = int(t)
            if num<0:
                negatives.append(num)
            total+=num

        if negatives:
            raise ValueError(f"negative numbers are not allowed:{','.join(map(str,negatives))}")
        
        return total