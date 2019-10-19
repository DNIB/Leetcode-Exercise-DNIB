class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r_node = l1
        c_node = r_node
        
        while c_node:
            c_node.val += l2.val
            if (c_node.next==None) and (l2.next or (c_node.val >= 10)):
                c_node.next = ListNode(int(c_node.val/10))
                c_node.val %= 10
            elif c_node.val >= 10 and c_node.next:
                c_node.next.val += int(c_node.val/10)
                c_node.val %= 10
            if l2.next == None:
                l2.next = ListNode(0)
            c_node, l2 = c_node.next, l2.next

        return r_node