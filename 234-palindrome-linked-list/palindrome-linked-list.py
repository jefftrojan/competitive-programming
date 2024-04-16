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
        temp = head
        store = []
        while temp:
            store.append(temp.val)
            temp = temp.next
        temp = head
        for i in range(len(store) -1, -1, -1):
            if temp.val != store[i]:
                return False
            temp = temp.next
        return True
        