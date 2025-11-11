class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def delete(self, head: ListNode) -> ListNode:
        # if list is empty or single node, return as is
        if not head or not head.next:
            return head
        
        # start with current node
        current = head
        
        # traverse the list
        while current and current.next:
            # if value equals the next value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # move to next node only if no duplicate
                current = current.next
                
        return head