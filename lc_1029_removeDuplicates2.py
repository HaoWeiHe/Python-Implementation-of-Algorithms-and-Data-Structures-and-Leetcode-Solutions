class Solution(object):
    def removeDuplicates(self, s, k):
        """
        deeedbbcccbdaa
        
        (d,0) (e,1)
        """
        
        
        stack = []
        
        for e in s:
            if not stack:
                stack.append((e,1))
            else:
                top_ele, top_count = stack[-1]
                if top_count == k-1 and top_ele == e:
                    for _ in range(k-1):
                        stack.pop()
                elif e == top_ele:
                    stack.append((e,top_count +1))
                else:
                    stack.append((e,1))
        return "".join([ele[0] for ele in stack])
     
