# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        def dfs(node, curr):
            
            # Base Case 1: If we have an empty tree
            if not node:
                return False
            
            # Base Case 2: We are at a leaf node
            if not node.left and not node.right:
                return curr + node.val == targetSum
            
            # Recursive case: We go down the left subtree and the right subtree
            return dfs(node.left, curr + node.val) or dfs(node.right, curr + node.val)

        
        return dfs(root, 0)
        