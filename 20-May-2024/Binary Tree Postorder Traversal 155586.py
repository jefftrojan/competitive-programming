# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = [(root, False)]
        res = []
        while stack:

            currentNode, visited = stack.pop()
            if not currentNode:
                continue
            if visited:
                res.append(currentNode.val)
            else:
                stack.append((currentNode, True))
                stack.append((currentNode.right, False))
                stack.append((currentNode.left, False))
        return res
        