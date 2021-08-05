# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        curr = head
        aftercurr = curr.next
        
        while aftercurr != None:
            if curr.val == aftercurr.val:
                curr.next = aftercurr.next
                aftercurr =  curr.next
            else:                    
                curr = curr.next
                aftercurr = curr.next

            
        return head