"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        #################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        def dfs(id):
            cur = employees[id-1]
            val, subs = cur.importance, cur.subordinates
            if not subs: return val
           
            h = [dfs(sid) for sid in subs:]
            return sum(h) + val
        return dfs(id)