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
        i = 0
        while i < len(some_list) and some_node is not None:
            if some_list[i] != some_node.val:
                return False
            i += 1
            some_node = some_node.next
        return i == len(some_list) and some_node is None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        last = head
        while last is not None and last.next is not None:
            tail = last.next
            while tail is not None and tail.val == last.val:
                tail = tail.next
            last.next = tail
            last = tail
        return head