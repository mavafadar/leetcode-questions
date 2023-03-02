# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists into a new sorted linked list.

    :param list1: Head of the first linked list.
    :type list1: ListNode
    :param list2: Head of the second linked list.
    :type list2: ListNode
    :return: Head of the merged linked list.
    :rtype: ListNode
        list1 (ListNode): 
        list2 (ListNode): 
    """
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    resultList = ListNode()
    resultListHelper = resultList
    while not list1 is None and not list2 is None:
        if list1.value >= list2.value:
            resultListHelper.value = list2.value
            list2 = list2.next
        else:
            resultListHelper.value = list1.value
            list1 = list1.next
        resultListHelper.next = ListNode()
        resultListHelper = resultListHelper.next
        

    if not list1 is None:
        resultListHelper.value = list1.value
        resultListHelper.next = list1.next
    if not list2 is None:
        resultListHelper.value = list2.value
        resultListHelper.next = list2.next
    if list1 is None and list2 is None:
        resultListHelper = None

    return resultList