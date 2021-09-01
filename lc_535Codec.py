class Codec:
    def __init__(self):
        self.en= {}
        self.de = {}
        self.counter = 0
    
    def encode(self, longUrl):
        """
        {123:1, }
        {1: 123}
        123 -> 1 
        
        1 -> 123
        """
        if longUrl not in self.en:
            self.counter += 1
            self.en[longUrl] = self.counter
            
        self.de[self.en[longUrl]] = longUrl
        
        return self.en[longUrl]
            
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.de[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))