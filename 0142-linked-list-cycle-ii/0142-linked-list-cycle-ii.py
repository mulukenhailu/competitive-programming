# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return
        
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
                
        if not fast.next or not fast.next.next:
            return 
                
        secondslow=head
        
        while slow.next:
            if slow==secondslow:
                return slow
            slow=slow.next
            secondslow=secondslow.next
            
        return 
        
            
            
        