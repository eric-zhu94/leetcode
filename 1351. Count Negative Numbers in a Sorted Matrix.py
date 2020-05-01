https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #O(mn) solution -> brute force by checking all elements in the matrix
        #bad because we do not use the non-decreasing benefit of the array
        #count = 0
        #for i in range(len(grid)):
        #    for j in range(len(grid[i])):
        #        if grid[i][j] < 0:
        #            count +=1
        #return count
        #Optimisation 1: iterate backwards, exiting as soon as we see a positive number
        #O(mn/2, assuming half elements are positive/ negative)
        #count = 0
        #for i in range(len(grid)):
        #    for j in range(len(grid[i]) - 1, -1, -1):
        #       if grid[i][j] < 0:
        #            count +=1
        #        else:
        #            break
        #return count
        #Better solution in O(mlogn) -> use binary search to find the number of negative elements in each row
        def bin_search(self, arr):
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] < 0:
                    end = mid - 1
                else:
                    start = mid + 1
            return len(arr) - start
        
        count = 0
        for row in range(len(grid)):
            count += bin_search(self, grid[row])      
        return count
        
