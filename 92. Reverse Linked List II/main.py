# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        addrList = []
        copyList = []
        present = head
        i = 0
        while present:
            if m-1 <= i < n:
                copyList.insert(0, present.val)
            addrList.append(present)
            i += 1
            present = present.next
        
        for i in range (m-1, n):
            addrList[i].val = copyList[0]
            del copyList[0]
            
        return addrList[0]
            