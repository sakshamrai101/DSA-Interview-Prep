143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
My solution: 
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second list
        second = slow.next
        prev = slow.next = None 
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge the two list. 
        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second 
            second.next = tmp1 
            first, second = tmp1, tmp2
