class Solution:
    def maxDepth(self , root ):
        if root == None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return l+1 if l >r else r+1