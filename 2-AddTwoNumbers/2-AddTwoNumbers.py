# Last updated: 22/10/2026, 4:44:11 pm
# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        list1 = []
        list2 = []
        while current1:
            try:
               
                list1.append(current1.val)
                current1 = current1.next
            except:
                print("out")
                break
        while current2:
            try:
                list2.append(current2.val)
                current2=current2.next
            except:
                print('out')
                break

        print(list1, list2)

        list1.reverse()
        list2.reverse()
        
        add1 = ""
        add2 = ""
        for addend in list1:
            add1 += (str(addend))
        for addend in list2:
            add2 += (str(addend))
        sums = int(add1) + int(add2)
        print(sums)

        final_list = []
        for char in str(sums):
            final_list.insert(0, int(char))
        print(final_list)

        final_link = ListNode(0)
        current = final_link

        for item in final_list:
            current.next = ListNode(item)
            current = current.next
        return final_link.next