class Solution:
    def hasPathSum(self , root , sum ):
        if not root:
            return False
        def dfs(root,sum,val):
            s1, s2 = False,False
            if not root.left and not root.right:
                if sum == val + root.val:
                    return True
                else:
                    return False
            if root.left:
                s1 = dfs(root.left,sum, val + root.val)
            if root.right:
                s2 = dfs(root.right,sum, val + root.val)
            return s1 or s2
        return dfs(root, sum, 0)