class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1. Find the middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split the list
        second = slow.next
        slow.next = None

        # 3. Reverse the second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 4. Merge the two halves
        first, second = head, prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2