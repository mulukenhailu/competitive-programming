# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack1=[]
        while head:
            stack1.append(head.val)
            head=head.next
        stack2=stack1[:]
        stack2.reverse()
        return stack1==stack2
        
#         start = head
        
#         while start:
#             print(start.val)
#             start=start.next
        
#         pre = None
#         while start:
            
#             temp = start
#             start = start.next
#             temp.next = pre
#             pre = temp
            
        # while head:
        #     print(head.val)
        #     head=head.next
            
#         while pre and head:
            
#             if pre.val != head.val :
#                 return False
#             pre = pre.next
#             head = head.next

#         return True
