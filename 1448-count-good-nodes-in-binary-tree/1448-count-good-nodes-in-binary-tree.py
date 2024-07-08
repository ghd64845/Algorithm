# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def DFS(node, prev):
            if not node:
                return
            
            if node.val >= prev:
                self.ans += 1
                
            max_val = max(node.val, prev)    
            DFS(node.left, max_val)
            DFS(node.right, max_val)
            
        DFS(root, root.val)
        return self.ans