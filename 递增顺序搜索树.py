class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        data = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            data.append(root)
            dfs(root.right)
        dfs(root)
        for i in range(len(data)):
            data[i].left = None
            data[i].right = data[i+1] if i<len(data)-1 else None
        return data[0]