class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def add_two_numbers(linked_list_one: ListNode, linked_list_two: ListNode) -> ListNode:
    """
    Takes two linked lists `linked_list_one` and `linked_list_two`, each representing a non-negative integer in reverse order, and returns a new linked list that represents the sum of the two numbers.

    :param linked_list_one: The first linked list representing a non-negative integer in reverse order.
    :type linked_list_one: ListNode
    :param linked_list_two: The second linked list representing a non-negative integer in reverse order.
    :type linked_list_two: ListNode
    :return: A new linked list representing the sum of the two numbers.
    :rtype: ListNode
    """
    number_one, number_two = str(), str()
    while linked_list_one is not None:
        number_one = str(linked_list_one.value) + number_one
        linked_list_one = linked_list_one.next
    while linked_list_two is not None:
        number_two = str(linked_list_two.value) + number_two
        linked_list_two = linked_list_two.next
    answer = str(int(number_one) + int(number_two))
    linked_list = ListNode()
    for index, character in enumerate(answer):
        linked_list.value = int(character)
        if index != len(answer) - 1:
            linked_list = ListNode(0, linked_list)
    return linked_list
