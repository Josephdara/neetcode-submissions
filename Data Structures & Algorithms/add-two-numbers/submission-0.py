# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list_out = ListNode()
        curr = list_out
        carryover = 0

        while l1 or l2 or carryover:
            x1 = l1.val if l1 is not None else 0
            x2 = l2.val if l2 is not None else 0

            new_curr = x1 + x2 + carryover
            carryover = new_curr // 10 # whole num multiple of 10
            new_curr = new_curr % 10 # whole num reminder, modulo
            curr.next = ListNode(new_curr)

            curr = curr.next
            l1 = l1.next if l1 else None  
            l2 = l2.next if l2 else None  
        return list_out.next
            


        
        