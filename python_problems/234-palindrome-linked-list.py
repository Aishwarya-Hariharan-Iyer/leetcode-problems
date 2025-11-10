# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head == None:
            return True

        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        
        l = len(arr)
        lp = 0
        rp = l-1

        while lp <= rp:
            if arr[lp] != arr[rp]:
                return False
            lp += 1
            rp -= 1

        return True
        
