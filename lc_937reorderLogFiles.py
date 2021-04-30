class Solution(object):
    def reorderLogFiles(self, logs):
        """
        1. ignore the identifier
        2. cmpare letter log
        3. remain the digit part
        """
        Ls, Ds = {},[]
        for e in logs:
            chunks = e.split(" ")
            if chunks[1].isdigit():
                Ds.append(e)
            else:
                Ls[e] = [" ".join(chunks[1:]) ,chunks[0]]
        
        return [e[0] for e in sorted(Ls.items(), key= lambda (k,v): (v[0],v[1]))]  + Ds
        
                