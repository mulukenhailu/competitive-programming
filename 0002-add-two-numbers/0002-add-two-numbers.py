# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        dum=ListNode(0)
        cur=dum
        while l1 or l2:
            carry=c
            if l1 and l2:
                carry+=(l1.val+l2.val)
                l1=l1.next
                l2=l2.next
            elif l1:
                carry+=l1.val
                l1=l1.next
            elif l2:
                carry+=l2.val
                l2=l2.next
            c=carry//10
            cur.next=ListNode(carry%10)
            cur=cur.next
        if c:
            cur.next=ListNode(1)
        return dum.next

            
        