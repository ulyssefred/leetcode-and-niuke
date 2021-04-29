class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 双指针法
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        i, j = 0,len(res)-1
        while i < j:
            if res[i]!=res[j]:
                return False
            i +=1
            j -=1
        return True
# 快慢指针法
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = None
        while slow:
            temp = slow.next
            slow.next = fast
            fast = slow
            slow = temp
        while fast:
            if fast.val != head.val:
                return False
            else:
                fast = fast.next
                head = head.next
        return True
#反转后半链表法
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = None
        while slow:
            slow.next, fast, slow = fast, slow, slow.next
        while fast:
            if fast.val != head.val:
                return False
            else:
                fast = fast.next
                head = head.next
        return True
