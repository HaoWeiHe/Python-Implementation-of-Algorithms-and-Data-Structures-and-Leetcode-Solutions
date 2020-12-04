class Solution:
    def pathSum(self, root,k):
        self.res = 0 
   
        def preorder(node, curr_sum, h):
            if not node:
                return 
            curr_sum += node.val
            if curr_sum == k:
                self.res +=1
            self.res += h[curr_sum - k]
            h[curr_sum] += 1
            preorder(node.left, curr_sum, h)
            preorder(node.right, curr_sum,h)
            h[curr_sum] -= 1

        # h = defaultdict(int)
        preorder(root, 0, defaultdict(int))
        return self.res


    def pathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.res = 0
        def dfs(node, score):
            if not node:
                return 
     
            if score == sum:
                self.res += 1
               
            if node.right:
                dfs(node.right, score + node.right.val)
            if node.left:
                dfs(node.left, score + node.left.val)
            
        def travel(node):
            if not node:
                return 
            
            dfs(node, node.val)
            travel(node.left)
            travel(node.right)
            

        travel(root)
        return self.res