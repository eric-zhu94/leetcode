class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xbit = []
        ybit = []
        ans = 0
        while x > 0:
            bit = x % 2
            x //= 2
            xbit.append(bit)
        while y > 0:
            bit = y % 2
            y //= 2
            ybit.append(bit)
        if len(xbit) > len(ybit):
            for i in range(len(xbit) - len(ybit)):
                ybit.append(0)
        if len(ybit) > len(xbit):
            for i in range(len(ybit) - len(xbit)):
                xbit.append(0)
        for j in range(len(xbit)):
            if xbit[j] != ybit[j]:
                ans +=1
        return ans
