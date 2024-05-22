# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = float('inf')
    height = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def find_left_val(root: Optional[TreeNode],height: int):

            if not root:
                return None

            left, right = find_left_val(root.left,height + 1), find_left_val(root.right, height + 1)
                
            if root and height > self.height and not (root.left or root.right):
                self.height = height
                self.val = root.val
            return root      
        find_left_val(root, self.height)
        return self.val if self.height > 0 else root.val 