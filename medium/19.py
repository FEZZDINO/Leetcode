# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or n <0:
            return None
        if head.next == None:
            return None
        p1, p2 = head, head

        while n>0:
            p1 = p1.next
            n-=1
        if not p1:          #n=number of nodes 
            return head.next  
        while p1.next:

            p2=p2.next
            p1=p1.next
        p2.next = p2.next.next
        
        
        return head