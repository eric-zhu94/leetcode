#https://leetcode.com/problems/two-sum-iii-data-structure-design/
class TwoSum:

    def __init__(self):
        self.numbers = {}
        """
        Initialize your data structure here.
        """
        

    def add(self, number: int) -> None:
        if number in self.numbers:
            self.numbers[number] += 1
        else:
            self.numbers[number] = 1
        """
        Add the number to an internal data structure..
        """
        

    def find(self, value: int) -> bool:
        for num in self.numbers.keys():
            rem = value - num
            if rem != num:
                if rem in self.numbers:
                    return True
            elif self.numbers[num] > 1:
                return True
        return False
            
            
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
