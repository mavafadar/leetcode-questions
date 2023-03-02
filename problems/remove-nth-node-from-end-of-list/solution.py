
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    Removes the n-th node from the end of a linked list and returns its head.

    :param head: The head node of the linked list.
    :type head: ListNode
    :param n: The index of the node to remove from the end, starting from 1.
    :type n: int
    :return: The head node of the modified linked list.
    :rtype: ListNode
    """
    if head is None or head.next is None and n == 1:
        return None
    
    nodesNumber = 0
    headHelper = head
    while not headHelper is None:
        headHelper = headHelper.next
        nodesNumber += 1

    targetNode = nodesNumber - n - 1
    if targetNode < 0:
        return head.next
    
    headHelper = head
    for _ in range(targetNode):
        headHelper = headHelper.next
    headHelper.next = headHelper.next.next
    
    return head