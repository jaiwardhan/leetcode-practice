class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def parse_into_node(some_list):
        head = None
        last = None
        for k in some_list:
            if head is None:
                head = ListNode(k, None)
                last = head
                continue
            last.next = ListNode(k, None)
            last = last.next
        return head

    @staticmethod
    def parse_from_node(some_node):
        res = []
        while some_node is not None:
            res.append(some_node.val)
            some_node = some_node.next
        return res

    @staticmethod
    def list_matches_node(some_list, some_node):
        matches = True
        i = 0
        while i < len(some_list) and some_node is not None:
            if some_list[i] != some_node.val:
                return False
            i += 1
            some_node = some_node.next
        return i == len(some_list) and some_node is None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        merged_node = None
        merged_node_last = None
        while l1 is not None and l2 is not None:
            ref_node_val = None
            if l1.val < l2.val:
                ref_node_val = l1.val 
                l1 = l1.next
            else:
                ref_node_val = l2.val
                l2 = l2.next
            if merged_node == None:
                merged_node = ListNode(ref_node_val, None)
                merged_node_last = merged_node
            else:
                merged_node_last.next = ListNode(ref_node_val)
                merged_node_last = merged_node_last.next
        
        if l1 is not None:
            if merged_node is None:
                merged_node = l1
            else:
                merged_node_last.next = l1
        if l2 is not None:
            if merged_node is None:
                merged_node = l2
            else:
                merged_node_last.next = l2
        return merged_node
            