# Definition for singly-linked list (you'll see this in LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to help build the result list
        dummy_head = ListNode(0)
        curr = dummy_head  # Current node we're building
        carry = 0          # Carry-over from previous addition
        
        # Process while we have nodes in either list OR there's a carry
        while l1 or l2 or carry:
            # Get current digits (0 if list ended)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Add digits + carry
            total = x + y + carry
            carry = total // 10  # New carry
            digit = total % 10   # Current digit
            
            # Create new node with current digit
            curr.next = ListNode(digit)
            curr = curr.next     # Move to next position
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next  # Skip dummy node and return result