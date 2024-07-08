# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        def DFS(node, arr):
            if not node: return
            if not node.left and not node.right:
                arr.append(node.val)
            
            DFS(node.left, arr)
            DFS(node.right, arr)
            
            return arr
        
        leaf1 = DFS(root1, [])
        leaf2 = DFS(root2, [])
        
        return leaf1 == leaf2