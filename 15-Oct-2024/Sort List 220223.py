# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        elements = []
        current = head
        while current:
            elements.append(current.val)
            current = current.next

        elements.sort()

        # Create a new sorted linked list
        sorted_head = ListNode(elements[0])
        current = sorted_head
        for val in elements[1:]:
            current.next = new_node = ListNode(val)
            current = new_node

        return sorted_head