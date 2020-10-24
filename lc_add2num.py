# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		root = dummy = ListNode(None)
		carry = 0
		
		while l1 or l2:
			carry, rem = divmod((l1.val + l2.val + carry),10)
			dummy.next = ListNode(rem)
			# carry = (l1.val + l2.val + carry)/10 
			dummy = dummy.next
			if (not l1.next) and (not l2.next) and not carry:
				break
			l1, l2 = l1.next if l1.next else ListNode(0), l2.next if l2.next else ListNode(0)

		return root.next
