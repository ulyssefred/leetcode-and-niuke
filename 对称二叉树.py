class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def rec(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return rec(left.left, right.right) and rec(left.right, right.left)
        return rec(root.left, root.right)