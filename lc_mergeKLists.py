from Queue import PriorityQueue


class Solution(object):
	def mergeKLists(self, lists):    
		root = cur = ListNode(None)
		h = PriorityQueue() 
		for node in lists:
			if node: h.put((node.val, node))

		while h.qsize() > 0:

			cur.next = h.get()[1]
			cur = cur.next
			if cur.next:
				h.put((cur.next.val, cur.next))
			
		return root.next