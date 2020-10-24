# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, val=0, next=None):
#		 self.val = val
#		 self.next = next

class ListNode():
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution(object):
	def __init__(self, ipt):
	
		head = dummy = ListNode()
		for e in ipt:
			dummy.next = ListNode(e)
			dummy  = dummy.next
		self.head = head

	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next: return head
		mid = self.getMid(head)
		lf = self.sortList(head)
		rt = self.sortList(mid)
		return self.merge(lf,rt)

	def getMid(self, head):
		slow, fast = head, head.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		
		start = slow.next
		slow.next = None
		return start

	def merge(self, p1,p2):
		dummy = head = ListNode()
		while p1 and p2:
			if p1.val < p2.val: 
				dummy.next = p1
				dummy = dummy.next
				p1 = p1.next
			else:
				dummy.next = p2
				dummy = dummy.next
				p2 = p2.next
		if p1: dummy.next = p1
		if p2: dummy.next = p2
		return head.next

Sol = Solution([4,2,1,3,8,9,10])
sorted_head = Sol.sortList(Sol.head)
res = []
while sorted_head:
	res.append(sorted_head.val)
	sorted_head =sorted_head.next
print(res)