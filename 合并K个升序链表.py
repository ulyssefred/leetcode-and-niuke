class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoLists(lists1,lists2):
            if not lists1 or not lists2:
                return lists1 if not lists2 else lists2
            pre = head = ListNode()
            a = lists1
            b = lists2
            while a and b:
                if a.val > b.val:
                    pre.next , pre, b= b, b, b.next
                else:
                    pre.next , pre, a= a, a, a.next
            if not a:
                pre.next = b
            else:
                pre.next = a
            return head.next
        def merge(lists,left, right):
            if left == right:
                return lists[left]
            mid = left + (right - left)//2
            lists1 = merge(lists,left,mid)
            lists2 = merge(lists,mid+1, right)
            return mergeTwoLists(lists1,lists2)
        if not lists:
            return None
        return merge(lists, 0, len(lists)-1)