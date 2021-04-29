class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def rebuildTree(self,pre_order_left,pre_order_right,in_order_left,in_order_right):
        if pre_order_left>pre_order_right:
            return None
        val = self.xianxu[pre_order_left]
        position = self.inorderdict[val]
        root = TreeNode(val)
        root.left = self.rebuildTree(pre_order_left+1, pre_order_left + position -in_order_left, in_order_left, position-1)
        root.right = self.rebuildTree(pre_order_left + position -in_order_left+1, pre_order_right, position+1, in_order_right)
        return root
    def solve(self , xianxu , zhongxu ):
        self.xianxu = xianxu
        self.zhongxu = zhongxu
        n = len(xianxu)
        if n == 0:
            return []
        self.inorderdict = {c:i for i,c in enumerate(zhongxu)}
        root = self.rebuildTree(0,n-1,0,n-1)
        rightview = []
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                if i == size-1:
                    rightview.append(cur_node.val)
        return rightview
test = Solution()
print(test.solve([1,2,4,5,3],[4,2,5,1,3]))