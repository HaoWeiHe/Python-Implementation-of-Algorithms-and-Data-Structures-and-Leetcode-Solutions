import hashlib

class Codec:
    def __init__(self):
        self.map = dict()
        
    def encode(self, longUrl):
        m = hashlib.md5()
        m.update(longUrl)
        h = m.hexdigest()
        self.map[h] = longUrl
        return h

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.map[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))