class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head :
            return head
        pre = self
        pre.next = head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                x = cur.val
                while cur.next and cur.next.val == x:
                    cur = cur.next
                pre.next, cur = cur.next, cur.next
            else:
                pre.next,pre,cur = cur, cur, cur.next
        return self.next