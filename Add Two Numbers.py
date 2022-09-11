def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        iter1 = l1.next
        iter2 = l2.next
        s = l1.val + l2.val
        carry = s//10
        s = s%10
        l3 = ListNode(s)
        iter3 = l3
        while iter1 != None and iter2 != None:
            s = iter1.val + iter2.val + carry
            carry = s//10
            s = s%10
            iter3.next = ListNode(s)
            iter1 = iter1.next
            iter2 = iter2.next
            iter3 = iter3.next
        while iter1 != None:
            s = iter1.val + carry
            carry = s//10
            s = s%10
            iter3.next = ListNode(s)
            iter1 = iter1.next
            iter3 = iter3.next
        while iter2 != None:
            s = iter2.val + carry
            carry = s//10
            s = s%10
            iter3.next = ListNode(s)
            iter2 = iter2.next
            iter3 = iter3.next
        if carry > 0:
            iter3.next = ListNode(carry)
        return l3
