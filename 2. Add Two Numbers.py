# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = []
        node = ListNode()
        ptr = node
        carry = 0
        while l1 is not None and l2 is not None:
            if carry == 1:
                if l1.val + l2.val + carry >= 10:
                    ans.append(l1.val + l2.val + carry - 10)
                else:
                    ans.append(l1.val + l2.val + carry)
                    carry = 0
            else:
                if l1.val + l2.val >= 10:
                    ans.append(l1.val + l2.val - 10)
                    carry = 1
                else:
                    ans.append(l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            if carry == 1:
                if l1.val + carry >= 10:
                    ans.append(l1.val + carry - 10)
                else:
                    ans.append(l1.val + carry)
                    carry = 0
            else:
                ans.append(l1.val)
            l1 = l1.next  
        while l2 is not None:
            if carry == 1:
                if l2.val + carry >= 10:
                    ans.append(l2.val + carry - 10)
                else:
                    ans.append(l2.val + carry)
                    carry = 0
            else:
                ans.append(l2.val)
            l2 = l2.next  
        if carry == 1:
            ans.append(1)
        for i in range(len(ans)):
            ptr.val = ans[i]
            if not i + 1 == len(ans):
                ptr.next = ListNode()
                ptr = ptr.next
        
        return node
            
        
