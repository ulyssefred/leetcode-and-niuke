# 给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，
# 打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，
# 但是其方向必须向下(只能从父节点指向子节点方向)。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        if not root:
            return 0

        def rec(root, cursum):
            if root.val == cursum:
                self.paths += 1
            if root.left: rec(root.left, cursum - root.val)
            if root.right: rec(root.right, cursum - root.val)

        def dfs(root, cursum):
            if not root:
                return
            rec(root, cursum)
            if root.left: dfs(root.left, cursum)
            if root.right: dfs(root.right, cursum)

        self.paths = 0
        dfs(root, sum)
        return self.paths