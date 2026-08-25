class ListNode:
    def __init__(self,val=0, next=None):
        self.val=val
        self.next= next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy

        carry = 0

        while l1 or l2 or carry:

            # Get values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add
            total = val1 + val2 + carry

            # Digit to store
            digit = total % 10

            # New carry
            carry = total // 10

            # Create node
            current.next = ListNode(digit)
            current = current.next

            # Move pointers
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next