import collections
class TreeNode(object):
    def __init__(self):
        self.child = collections.defaultdict(TreeNode)
        self.isSentence = False
        self.frequency = 0
        self.Sentence = ""

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        self.query = ""
        self.root = TreeNode() 
        for i,stn in enumerate(sentences):
            freq = times[i]
            self.insert_Sentence(stn, freq)        

    def insert_Sentence(self, stn,freq):
        node = self.root
        for ele in stn:
            node = node.child[ele] # {i:{" ":{#},"s":{#}}}
        node.isSentence = True
        node.frequency += freq
        node.Sentence = stn
        # print(stn, "insered",node.Sentence)

    def getTop3(self,terms):
          
        sort_ans = sorted(terms, key = lambda x: (-x.frequency, x.Sentence), )
        # print(sort_ans)
        # for e in sort_ans[:3]:
            # print(e.Sentence, e.frequency)
        return [e.Sentence for e in sort_ans[:3]]
        # if same, sort again
        # 2 sorted
    def search_sentence(self,prefix):
        node = self.root
        self.res =[] #Node


        def helper(node):
            if node.isSentence:
                self.res.append(node)
                # print(node.Sentence)
            for e in node.child: #{i:{nodes}}
                # print(e)
                if e !="#":
                    helper(node.child[e])
                    # helper(node)
           
            # return res

        for char in prefix:
            if char not in node.child: return []
            node = node.child[char]
        helper(node)
        return self.getTop3(self.res)
        #sort_res = sorted(self.res, key = lambda x: (x.frequency, sum(x.Sentence)), reverse= True)
        # print([(x.Sentence, x.frequency) for x in sort_res])
        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        
        if c =="#":
            self.insert_Sentence(self.query, 1)
            self.query = ""
            return []
        else:
            self.query += c
            return self.search_sentence(self.query)

# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
sentences = ["i love you","island", "ironman","i love leetcode"  ]
times = [5,3,2,2]
auto = AutocompleteSystem(sentences, times)
print(auto.input("i"))
print(auto.input(" "))
print(auto.input("a"),"Re")

print(auto.input("#"),"re")
print(auto.input("i"))
print(auto.input(" "))
print(auto.input("a"))

print(auto.input("#"))
print(auto.input("i"))
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)