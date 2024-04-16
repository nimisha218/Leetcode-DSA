# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        ans = []
        
        queue = deque([root])

        while queue:

            nodes_at_level = len(queue)

            curr_max = float("-inf")

            for _ in range(nodes_at_level):

                curr_node = queue.popleft()

                curr_max = max(curr_max, curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)

            ans.append(curr_max)
        
        return ans

        