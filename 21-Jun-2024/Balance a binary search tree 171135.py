# Problem: Balance a binary search tree - https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bst(self, nums, i, j):
        if i > j:
            return None
        mid = (i+j) // 2
        node = TreeNode(nums[mid])
        node.left = self.bst(nums, i, mid-1)
        node.right = self.bst(nums, mid+1, j)
        return node
    
    def dfs(self, node):
        if not node:
            return []
        l, r = self.dfs(node.left), self.dfs(node.right)
        return l + [node.val] + r
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.dfs(root)
        return self.bst(nums, 0, len(nums)-1)