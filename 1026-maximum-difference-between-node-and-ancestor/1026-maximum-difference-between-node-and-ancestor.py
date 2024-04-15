# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs_low(node, anc, maxDiff):

            if not node:
                return maxDiff
            
            if node.left == None and node.right == None:
                return max(maxDiff, abs(node.val - anc))
            
            maxDiff = max(maxDiff, abs(node.val - anc), dfs_low(node.left, min(node.val, anc), max(maxDiff, abs(node.val - anc))), dfs_low(node.right, min(node.val, anc), max(maxDiff, abs(node.val - anc))))

            return maxDiff
        
        def dfs_high(node, anc, maxDiff):

            if not node:
                return maxDiff

            if node.left == None and node.right == None:
                return max(maxDiff, abs(node.val - anc))
            
            maxDiff = max(maxDiff, abs(node.val - anc), dfs_high(node.left, max(node.val, anc), max(maxDiff, abs(node.val - anc))), dfs_high(node.right, max(node.val, anc), max(maxDiff, abs(node.val - anc))))

            return maxDiff

        return max(dfs_low(root, root.val, float("-inf")), dfs_high(root, root.val, float("-inf")))