# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        traversal = []
        queue = [root]
        while queue:
            node = queue.pop()
            traversal.append(node.val)
            for next_node in [node.right, node.left]:
                if next_node:
                    queue.append(next_node)

        return traversal