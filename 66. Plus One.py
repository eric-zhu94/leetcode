class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits)
        if digits[ptr - 1] != 9:
            digits[ptr - 1] += 1
            return digits
        else:
            #case when need to add another tens place vs no need
            while digits[ptr - 1] == 9:
                digits[ptr - 1] = 0
                #check if next decimal place exists
                if (ptr - 2) < 0:
                    digits.insert(0, 1)
                elif digits[ptr - 2] == 9:
                    ptr -=1
                    continue
                else:
                    digits[ptr -2] +=1
                    return digits
            return digits
                    
                    

                
