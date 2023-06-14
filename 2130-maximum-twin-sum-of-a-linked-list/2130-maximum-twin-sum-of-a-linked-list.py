# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        stack2=[]
        while head:
            stack.append(head.val)
            head=head.next
        for i in range(len(stack)//2):
            stack2.append(stack[i]+stack[len(stack)-1-i])
            
        return max(stack2)
            
        
        