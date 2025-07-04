###     This is stringCalculator.py     ###

class StringCalculator:
    def Add(self,numbers:str)->int:
        if numbers == "":
            return 0
        
        parts = numbers.split(",")
        return sum(int(p) for p in parts)