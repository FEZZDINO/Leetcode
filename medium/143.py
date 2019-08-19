# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def seperate_list(head):
    beg = end = head 
    while end and end.next:
        beg = beg.next
        end = end.next.next

    middle = beg.next
    beg.next = None

    return middle

def reverse_list(node):
    last = None
    currentNode = node
    
    while currentNode:
        curnext = currentNode.next
        currentNode.next = last
        last = currentNode
        currentNode = curnext
    return last
def merge_list(a, b):
    new = a
    while b:
        a.next, a = b, a.next
        b.next, b = a, b.next
    return new
        

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return 
        print(1)
        mid = seperate_list(head)
        
        mid = reverse_list(mid)
        head = merge_list(head, mid)