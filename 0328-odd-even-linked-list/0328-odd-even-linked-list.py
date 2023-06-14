# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        odd=head
        dummyodd=ListNode(0)
        temp1=dummyodd
        while odd and odd.next:
            temp1.next=ListNode(odd.val)
            temp1=temp1.next
            odd=odd.next.next
        if odd:
            temp1.next=ListNode(odd.val) 
            temp1=temp1.next
            
        even=head.next
        dummyeven=ListNode(0)
        temp2=dummyeven
        while even and even.next:
            temp2.next=ListNode(even.val)
            temp2=temp2.next
            even=even.next.next
        if even:
            temp2.next=ListNode(even.val)
        
        temp3=dummyeven.next
            
        temp1.next=temp3
        
        return dummyodd.next
            
#         if not head:
#             return head
#         counter=1
#         dummy=ListNode(0)
#         temp=dummy
#         temp2=dummy
#         dummy1=ListNode(0)
#         temp1=dummy1
#         while head:
#             if counter%2!=0:
#                 temp.next=ListNode(head.val)
#                 temp=temp.next
#             else:
#                 temp1.next=ListNode(head.val)
#                 temp1=temp1.next
#             counter+=1
#             head=head.next
#         while temp2.next:
#             temp2=temp2.next
#         temp2.next=dummy1.next
        
#         return dummy.next
        