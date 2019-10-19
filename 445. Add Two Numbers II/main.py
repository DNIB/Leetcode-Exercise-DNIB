# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = 0, 0
        while l1:
            n1 *= 10
            n1 += l1.val
            l1 = l1.next
        while l2:
            n2 *= 10
            n2 += l2.val
            l2 = l2.next
        n3 = n1+n2
        n4 = 0
        i = 0
            
        while n3>0:
            n4 *= 10
            n4 += n3%10
            n3 /= 10
            i += 1
        
        r_node = ListNode(0)
        c_node = r_node
        runned = None
        while n4>0 or (runned == None) or i>0:
            c_node.next = ListNode(n4%10)
            c_node = c_node.next
            n4 /= 10
            runned = True
            i -= 1
        
        return r_node.next