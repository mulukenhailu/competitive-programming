# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dum=head
        length=1
        while dum.next:
            length +=1
            dum=dum.next
        
        if length==n:
            temp=head.next
            return temp
        
        dum2=head
        k=length-n-1
        while k>0:
            dum2=dum2.next
            k-=1
        if dum2.next:
            dum2.next=dum2.next.next
        else:
            dum2.next=None
        
        return head
            
        