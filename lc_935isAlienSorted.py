class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {word:idx for idx, word in enumerate(order)}
        
        n_words = len(words)
        def compare(A,B):
            for i in range(len(A)):
                if i >= len(B):
                    return False
                if d[A[i]] < d[B[i]] :
                    return True
                elif d[A[i]] == d[B[i]]:
                    continue
                else:
                    return False
            return True
           


        for i in range(n_words-1):
            A_word, B_word = words[i], words[i+1]
            if not compare(A_word, B_word):
                return False
        return True

