# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sort = list1

        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val > list2.val:
            sort = list2
            list2 = list2.next
        else:
            list1 = list1.next

        head = sort

        while list1 and list2:
            if list1.val < list2.val:
                sort.next = list1
                list1 = list1.next
            else:
                sort.next = list2
                list2 = list2.next

            sort = sort.next

        if list1:
            sort.next = list1
        elif list2:
            sort.next = list2

        return head