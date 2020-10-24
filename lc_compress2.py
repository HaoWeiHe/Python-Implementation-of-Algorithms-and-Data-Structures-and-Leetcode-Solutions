class Solution(object):
	def compress(self, chars):
       


def inplace_write_length(arr):
	pr, pw = 0, 0
	while True:
		# reading
		if pr == len(arr):
			break
		count = 0
		while arr[pr+count] == arr[pr]:
			count += 1
			if pr + count == len(arr):
				break
		pr += count
		# writing
		chars = list(str(count))
		for i, c in enumerate(chars):
arr[pw+1+i] = c
pw += 1 + len(chars)
	while len(arr) > pw:
		arr.pop(-1)