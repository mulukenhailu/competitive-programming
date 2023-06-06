# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        where_i_am=node
        copy_of_my_next=node.next
        where_i_am.val=copy_of_my_next.val
        where_i_am.next=where_i_am.next.next

        
        