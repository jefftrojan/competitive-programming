# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base cases
        if head is None or k == 0:
            return head
        if head.next is None:
            return head
        
        # get end of list as well as length of list
        temp = head
        nodeCount = 1
        while temp.next != None:
            temp = temp.next
            nodeCount += 1
        tail = temp

        # connect end of list to head
        tail.next = head

        # find the node to shift from
        k = k % nodeCount
        shifts = nodeCount - k - 1
        temp = head
        while shifts > 0:
            temp = temp.next    
            shifts -= 1

        # reset head and cut connection to break loop
        head = temp.next
        temp.next = None

        return head