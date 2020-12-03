
class Solution(object):
	def search(self, nums, target):
		"""
		case 1) mid locate on the right part
         /
		/
             ,/ <- mid 
            /
            in this case, 
            if target locates after mid, l = m +1
		    else r = m -1

		case 2) mid locate on the left part
	    ,/
	   /           <- mid 
	             /
	            /
	    in this case, if target locates before mid, r = m -1
	    else l = m +1   
		"""
		l, r = 0, len(nums)-1
		
		while l <= r:
			mid = (l+r)//2
			if nums[mid] == target:
				return mid

			if nums[l] <= nums[mid]:
				if nums[l] <= target < nums[mid]:
					r = mid - 1
				else:
					l = mid + 1
			else:
				if nums[mid] < target <= nums[r]:
					l = mid +1
				else:
					r = mid -1
		return -1
