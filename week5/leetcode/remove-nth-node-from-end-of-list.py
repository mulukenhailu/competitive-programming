# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # two pointer methods 2/12/2024  a2sv boot camp
        fast = head
        slow = head

        # Move fast pointer to the nth node from the beginning
        for _ in range(n):
            fast = fast.next

        # If fast becomes None, it means n is equal to the number of nodes in the list
        # So, we need to remove the head node
        if not fast:
            return head.next

        # Move both pointers until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return head



        