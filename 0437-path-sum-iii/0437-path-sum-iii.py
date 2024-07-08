# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        def DFS(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            
            path_count = path_counts[curr_sum - targetSum]
            
            path_counts[curr_sum] += 1
            
            path_count += DFS(node.left, curr_sum)
            path_count += DFS(node.right, curr_sum)
            
            path_counts[curr_sum] -= 1
          
            return path_count
            
                
            
        path_counts = Counter({0: 1})
        
        return DFS(root, 0)