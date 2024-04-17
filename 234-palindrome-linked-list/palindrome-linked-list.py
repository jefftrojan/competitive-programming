# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head 
        while fast and fast.next:
           fast = fast.next.next
           slow = slow.next 
            
        stack1=[]
        stack2 = []
        
        fast = slow 
        slow = head
        while fast:
            stack2.append(slow.val)
            stack1.append(fast.val)
            fast = fast.next
            slow = slow.next 
            
        stack2.reverse()
        return stack1 == stack2
        