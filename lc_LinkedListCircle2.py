class Solution:

	def detectCycle(self, head):
		if head == None or head.next == None:
			return None
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			# if fast == slow:
				# break
			if slow == fast:
				slow = head
				while slow != fast:
					slow = slow.next
					fast = fast.next
				return slow
		return None