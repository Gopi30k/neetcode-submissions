# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def validate(self, node: Optional[TreeNode], min_val, max_val):
        if node is None:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return self.validate(node.left, min_val, node.val) and self.validate(node.right, node.val, max_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('+inf'))