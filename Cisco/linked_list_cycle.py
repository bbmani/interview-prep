def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    visited_nodes = list()
    while head is not None:
        if head in visited_nodes:
            return True
        else:
            visited_nodes.append(head)
        head = head.next

    
    
    return False