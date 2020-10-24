import collections
class Solution(object):
	def isNStraightHand(self, hand, W):
		"""
		:type hand: List[int]
		:type W: int
		:rtype: bool
		"""
		if len(hand) % W != 0 : return False
		sord_hand = sorted(list(set(hand)))
		C  = collections.Counter(hand)
		for i in sord_hand:
			while C[i] >0:
				for dx in range(W):
					if not C[i+dx]: return False
					C[i+ dx] -=1
		return True

hand = [1,2,3,4,5,6]#[1,2,3,6,2,4,7,8]
W = 2


print(Solution().isNStraightHand(hand, W))