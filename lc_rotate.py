class Solution(object):
	def rotate(self, matrix):
		matrix[::] = matrix[::-1]
		n = len(matrix)
		for i in range(n):
			for j in range(i+1, n):
				
				tmp = matrix[i][j]
				matrix[i][j] = matrix[j][i]
				matrix[j][i] = tmp

	# print(matrix)