# slow moves 1 step at a time, fast moves 2 steps at a time.
# when slow and fast meet each other, they must be on the cycle

# when x,y meet, slow traveled (x + y) steps while fast traveled 2 * (x + y) steps, 
# and the extra distance (x + y) must be a multiple of the circle length C
# so x + y = N * C, 
# let fast continue to travel from y and after x more steps, slow will appear at the start of the cycle.
# Since the distance from head to cycle is x steps, so move slow to head and moves x steps to meet fast.


def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow =head
        fast= head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
