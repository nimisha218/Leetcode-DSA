# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxSoFar):
            
            # Base Case 1: No nodes, no good nodes
            if not node:
                return 0
        
            # Go down the left sub-tree while keeping a tab on the maxSoFar
            left = dfs(node.left, max(node.val, maxSoFar))
            # Go down the right sub-tree while keeping a tab on the maxSoFar
            right = dfs(node.right, max(node.val, maxSoFar))
            
            # Compute the sum of left and right
            ans = left + right
            
            # CHeck if the current node is also a good node
            if node.val >= maxSoFar:
                ans += 1
            
            # Return the answer
            return ans
        
        return dfs(root, float("-inf"))
            