# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s = 0 

        def dfs(node, parent, grandparent):
            nonlocal s 

            if node is None:
                return 

            if grandparent is not None and grandparent.val % 2 == 0:
                s += node.val 

            dfs(node.left, node, parent)
            dfs(node.right, node, parent) 

        dfs(root, None, None) 
        return s