# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTarget(self,root,target):
        if root is None:
            return float("infinity"),''
        if root==target:
            return 0,''
        x,path1=self.getTarget(root.left,target)
        y,path2=self.getTarget(root.right,target)
        if x<y:
            return x+1,'L'+path1
        else:
            return y+1,'R'+path2

    def addNeighbor(self,root,k,path,lst,lvl,target):
        if root is None:
            return
        if path=='':
            if k==lvl:
                lst.append(root.val)
                return
            self.addNeighbor(root.left,k,path,lst,lvl+1,target)
            self.addNeighbor(root.right,k,path,lst,lvl+1,target)
            return
        x=path[0]
        if k==lvl:
            lst.append(root.val)
        if x=='L':
            self.addNeighbor(root.left,k,path[1:],lst,lvl-1,target)
            self.addNeighbor(root.right,k,'',lst,lvl+1,target)
        else:
            self.addNeighbor(root.right,k,path[1:],lst,lvl-1,target)
            self.addNeighbor(root.left,k,'',lst,lvl+1,target)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        lvl,path=self.getTarget(root,target)
        lst=[]
        self.addNeighbor(root,k,path,lst,lvl,target)
        return lst