class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxres = float("-inf")
        def dfs(node):
            if not node:
                return 0
            leftmax = max(dfs(node.left),0)
            rightmax = max(dfs(node.right),0)
            curmax = node.val+leftmax+rightmax
            self.maxres = max(curmax,self.maxres)
            return node.val +max(leftmax,rightmax)
        dfs(root)
        return self.maxres