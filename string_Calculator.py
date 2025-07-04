###     This is stringCalculator.py     ###

#   --- importing re for usage of reguler exp for ','|'\n' 
import re

class StringCalculator:
    def Add(self,numbers:str)->int:
        if numbers == "":
            return 0
        
        parts = re.split(r",|\n",numbers)
        return sum(int(p) for p in parts)