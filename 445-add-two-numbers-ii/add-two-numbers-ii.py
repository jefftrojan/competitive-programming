# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        # Reverse l1 and l2
        l1, l2 = reverse(l1), reverse(l2)
        dummy = ListNode(0)
        temp = dummy
        reminder = 0
        while l1 and l2:
            sumVal = l1.val + l2.val + reminder
            reminder = sumVal // 10
            temp.next = ListNode(sumVal % 10)
            temp = temp.next
            l1, l2 = l1.next, l2.next
        
        pend = l1 if l1 else l2
        while pend:
            sumVal = pend.val + reminder
            reminder = sumVal // 10
            temp.next = ListNode(sumVal % 10)
            temp = temp.next
            pend = pend.next
        
        if reminder > 0:
            temp.next = ListNode(reminder)

        return reverse(dummy.next)
        