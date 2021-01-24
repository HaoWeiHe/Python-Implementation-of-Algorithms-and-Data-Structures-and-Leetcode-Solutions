class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        g = collections.defaultdict(list)
        for e in strs:
            g[tuple(sorted(e))].append(e)
        return g.values()