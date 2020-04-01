class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1
            return arr
        else:
            hi = arr[len(arr) - 1]
            for i in range(len(arr) -2, -1,-1):
                tmp = arr[i]
                arr[i] = hi
                if tmp > hi:
                    hi = tmp
            arr[len(arr) - 1] = -1
            return arr
