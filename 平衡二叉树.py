class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 后序递归
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def aftersort(root):
            if not root:
                return 0
            left = aftersort(root.left)
            # 减支
            if left == -1:
                return -1
            right = aftersort(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return aftersort(root) != -1
# 普通计算depth
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root :
            return True
        return abs(self.depth(root.left)- self.depth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self,root):
        if not root:
            return 0
        return max(self.depth(root.left),self.depth(root.right)) + 1