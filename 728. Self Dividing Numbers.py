https://leetcode.com/problems/self-dividing-numbers/
def selfDividingNumbers(self, left: int, right: int) -> List[int]:
  return [num for num in range(left, right + 1) if '0' not in str(num) and all([num % int(d) == 0 for d in str(num)])]
