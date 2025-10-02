# start by initializing a dummy node, create a dummy head for the result list

# use two pointers to track the current nodes in list1 and list 2, add the similar value to the result

# if one list is exhausted, append te rest of the other list

# return the next node of the dummy head

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, list1, list2):
        # step 1: create a dummy node
        dummy = ListNode(0)
        current = dummy
        
        # traverse both lists while both have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
                
        # attach the remaining nodes of list1, if any 
        if list1:
            current.next = list1
            
        # attach the remaining nodes of list2, if any
        if list2:
            current.next = list2
            
        return dummy.next
        