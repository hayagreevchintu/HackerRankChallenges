# Complete the printLinkedList function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
#Solution begins here:
def printLinkedList(head):
    while head != None:
        print(head.data)
        head = head.next