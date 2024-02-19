# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1=ListNode(0)
        dummy2=ListNode(0)
        cur1=dummy1
        cur2=dummy2
        ptr=head

        while ptr:
            if ptr.val<x:
                cur1.next=ptr
                cur1=cur1.next

            else:
                cur2.next=ptr
                cur2=cur2.next

            ptr=ptr.next

        cur2.next=None
        cur1.next=dummy2.next

        return dummy1.next
        