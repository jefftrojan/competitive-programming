# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        back = head 
        front = head.next 

        stop = 0

        while front:
            if back.val > front.val:
                back.val, front.val = front.val, back.val 
            back = back.next 
            front = front.next 
            stop += 1
        
        for _ in range(stop): 
            back = head 
            front = head.next 

            while front:
                if back.val > front.val:
                    back.val, front.val = front.val, back.val 
                back = back.next 
                front = front.next

        return head