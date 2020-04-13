https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return
        elif root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return NULL
