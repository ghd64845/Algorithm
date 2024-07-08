# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        visited = [0]
        
        def DFS(node):
            if node is None:
                return 0
            else:
                l_depth = DFS(node.left)
                r_depth = DFS(node.right)
                
                if (l_depth > r_depth):
                    return l_depth+1
                else:
                    return r_depth+1
            
            
        return DFS(root)
        
        
        
        