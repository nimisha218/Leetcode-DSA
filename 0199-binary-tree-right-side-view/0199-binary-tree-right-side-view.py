# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:

            nodes_at_level = len(queue)

            ans.append(queue[-1].val)

            for _ in range(nodes_at_level):
                
                current_node = queue.popleft()

                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)
        
        return ans


