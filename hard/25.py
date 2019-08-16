# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        count = 0
        while curr != None and count != k: #find the k+1 node
            curr = curr.next
            count+=1
        if count == k:                      #if k+1 node is found
            curr = self.reverseKGroup(curr, k)  #reverse list with k+1 node as head
            #head - head-pointer to direct part, 
            #curr - head-pointer to reversed part
            while count>0:  #reverse current k-group:
                tmp = head.next #tmp - next head in direct part
                
                head.next = curr    #preappending "direct" head to the reversed list 
                
                curr = head     #move head of reversed part to a new node
                head = tmp      #move "direct" head to the next node in direct part
                count-=1
            head = curr
        #print(head)
        return head