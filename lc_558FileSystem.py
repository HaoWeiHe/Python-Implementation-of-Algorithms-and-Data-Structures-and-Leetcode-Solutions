"""
trie structure? 
a -> b -> c 
ls : go to the dir and print the child
mkdir: make the path throughout the given path
content: print the contend if found

{foo: {xoo: {zoo:Node, yoo: Node} }}
Node:
    content
Trie: 
    root_of_Node
    children
/a/b/c
/a/b/c ls?
c!
/ ls?
 -> a
/a ls?
  -> b
"""
class Node():
    def __init__(self):
        self.content = ""
        self.children = defaultdict(Node)
        self.isFile = False
        self.filename = ""
        
class Trie():
    def __init__(self):
        self.root = Node()
        
    def insert(self,paths):
        node = self.root
        for e in paths:
            if e == "":
                continue
            node = node.children[e] 
        return node
    
    def insertfile(self,paths):
        node = self.insert(paths)
        name = paths[-1]
        node.isFile = True
        node.filename = name
        return node
    
class FileSystem(object):
    
    def __init__(self):
        trie = Trie()
        self.trie = trie
        self.root = trie.root
        
    def get_subpaths(self, path):
        return path.split("/")
                          
    def ls(self, path):
        """
        *go the the direction and list all of the child
        """
        paths = self.get_subpaths(path)
        node = self.trie.insert(paths)
        if node.isFile:
            
            return [node.filename]
        return  sorted(node.children.keys())

    def mkdir(self, path):
        """
        traversal the tree
        """
        paths = self.get_subpaths(path)
        self.trie.insert(paths)
        
    def addContentToFile(self, filePath, content):
        """
        go to the filepath and append content
        """
        paths = self.get_subpaths(filePath)
        node = self.trie.insertfile(paths)
        node.content+= content

    def readContentFromFile(self, filePath):
        """
        print the content which exist on the fildPath
        """
        paths = self.get_subpaths(filePath)
        node = self.trie.insert(paths)
        return node.content
                               
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)