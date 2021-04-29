class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return None
        list1 = []
        pre = head
        while pre:
            list1.append(pre)
            pre = pre.next
        i, j = 0,len(list1)-1
        while i<j:
            list1[i].next = list1[j]
            i +=1
            if i == j:
                break
            list1[j].next = list1[i]
            j-=1
        list1[i].next = None
        # 2
        class Solution:
            def reorderList(self, head: ListNode) -> None:
                if not head:
                    return

                mid = self.middleNode(head)
                l1 = head
                l2 = mid.next
                mid.next = None
                l2 = self.reverseList(l2)
                self.mergeList(l1, l2)

            def middleNode(self, head: ListNode) -> ListNode:
                slow = fast = head
                while fast.next and fast.next.next:
                    slow = slow.next
                    fast = fast.next.next
                return slow

            def reverseList(self, head: ListNode) -> ListNode:
                prev = None
                curr = head
                while curr:
                    nextTemp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nextTemp
                return prev

            def mergeList(self, l1: ListNode, l2: ListNode):
                while l1 and l2:
                    l1_tmp = l1.next
                    l2_tmp = l2.next

                    l1.next = l2
                    l1 = l1_tmp

                    l2.next = l1
                    l2 = l2_tmp
