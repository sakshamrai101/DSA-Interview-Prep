19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy Node to return the list. 
        dummy = ListNode(0, head)
        left = dummy 
        right = head


        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next


        # delete the node
        left.next = left.next.next
        return dummy.next
