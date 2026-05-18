# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            return 1+max(left,right)
        def is_balanced(node):
            if node is None:
                return True

            left = height(node.left)
            right = height(node.right)

            if abs(left - right) > 1:
                return False

            return is_balanced(node.left) and is_balanced(node.right)
        
        return is_balanced(root)