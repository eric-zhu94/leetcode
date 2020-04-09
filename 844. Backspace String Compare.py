#https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a_stack = []
        b_stack = []
        for c in S:
            if c == "#":
                if len(a_stack) != 0:
                    a_stack.pop()
            else:
                a_stack.append(c)
        for c in T:
            if c == "#":
                if len(b_stack) != 0:
                    b_stack.pop()
            else:
                b_stack.append(c)
        if len(a_stack) != len(b_stack):
            return False
        else:
            start = 0
            for i in range(len(a_stack)):
                if a_stack[i] != b_stack[i]:
                    return False
            return True
