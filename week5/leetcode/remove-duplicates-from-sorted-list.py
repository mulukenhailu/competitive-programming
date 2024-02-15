# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        cur=head
        ptr=cur.next

        while cur:
            while ptr and ptr.val==cur.val:
                ptr=ptr.next
            cur.next=ptr
            cur=cur.next
        return head






        