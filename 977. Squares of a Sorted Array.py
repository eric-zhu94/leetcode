class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        start = 0
        end = len(A) - 1
        ans = []
        while start < end:
            if abs(A[end]) == abs(A[start]):
                ans.append(A[end] ** 2)
                ans.append(A[start] ** 2)
                start +=1
                end -= 1
            elif abs(A[end]) > abs(A[start]):
                ans.append(A[end] ** 2)
                end -= 1
            else:
                ans.append(A[start] ** 2)
                start += 1
        if len(ans) != len(A):
            ans.append(A[start] ** 2)
        
        
        return ans[::-1]
        
