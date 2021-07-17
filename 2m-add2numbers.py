#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
       def addTwoNumbers(self, l1: ListNode, l2: ListNode, nextdig = 0) -> ListNode:
        outlist = ListNode()
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
            
        total = val1 + val2 + nextdig
        outlist.val += total % 10 
        nextdig = total // 10

        if nextdig != 0:
            outlist.next = ListNode(nextdig)


        if l1.next != None or l2.next != None:
            outlist.next = self.addTwoNumbers(l1.next if l1.next else ListNode(), 
            l2.next if l2.next else ListNode(), nextdig)
        return outlist
        
        return outlist
list1 = ListNode(1)
list1.next = ListNode(2)

list2 = ListNode(2)
list2.next = ListNode(9)
# curr = list1
# while curr != None:
#     print(curr.val)
#     curr = curr.next

test = Solution()
joe = test.addTwoNumbers(list1, list2)

while joe != None:
    print("The value is: ",joe.val)
    joe = joe.next



