# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bits = []
        ans = 0
        while head:
            bits.append(head.val)
            head = head.next
        pw = 0
        while len(bits):
            ans += bits.pop() * 2 ** pw
            pw +=1
        return ans
            
        
        
    
