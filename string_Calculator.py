#   --- importing re for usage of reguler exp for ','|'\n' 
import re

class StringCalculator:

    ### defining a constructor for call count
    def __init__(self):
        self.call_count = 0

    def Add(self,numbers:str)->int:
        self.call_count += 1
        if numbers == "":
            return 0
        
        delimeter_pattern = r",|\n"

        if numbers.startswith("//"):
            parts = numbers.split("\n",1)
            delimeter = parts[0][2:]
            numbers = parts[1]

            if delimeter.startswith("[") and delimeter.endswith("]"):
                delimeters = re.findall(r"\[(.*?)\]", delimeter)  # fixed typo in variable use
                delimeter_pattern = "|".join(re.escape(d) for d in delimeters)
            else:
                # Single character delimiter (like //;\n)
                delimeter_pattern = re.escape(delimeter)
        
        tocken = re.split(delimeter_pattern,numbers)

        total = 0
        negatives = []

        for t in tocken:
            t = t.strip()
            if not t:
                continue
            num = int(t)
            if num<0:
                negatives.append(num)
            elif num>1000:
                num = 0
            total+=num

        if negatives:
            raise ValueError(f"negative numbers are not allowed:{','.join(map(str,negatives))}")
        
        return total
    
    ### defining a method GetCalledCount will return count of how many times Add() called
    def GetCalledCount(self):
        return self.call_count
