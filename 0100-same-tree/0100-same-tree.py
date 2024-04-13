# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base Case 1: Both trees are empty
        if not p and not q:
            return True
        
        # Base Case 2: Either of the trees are non empty
        if not p or not q:
            return False
        
        # Recursive Case (go left and right both)
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        