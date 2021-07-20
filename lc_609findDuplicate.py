class Solution(object):
    def findDuplicate(self, paths):
        """
["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
"root/a 1.txt(abcd) 2.txt(efgh)" -> 1.txt(abcd), 2.txt(efgh)
abcd) :[root/a + "/" + 1.txt,root/c + "/" + 3.txt] 
efgh): [root/a + "/" + 2.txt] 

"root/c 3.txt(abcd)"
abcd):[]

        """
        d = defaultdict(list)
        for path in paths:
            eles = path.split(" ")
            root = eles[0]
            for ele in eles[1:]:
                f, key = ele.split("(")
                d[key].append(root + "/" + f)
        return [ x for x in d.values() if len(x) > 1]
        