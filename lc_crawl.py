# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        seed =startUrl # htmlParser.getUrls(startUrl)
       
        q = [seed]
        res = []
        prefix = startUrl.split("/")[2]
        visted = {startUrl}
        while q:
            top = q.pop(0)
            # print(q)
            if prefix in top:
                res.append(top)
            
            deeper = htmlParser.getUrls(top)
            for ele in deeper:
                print(ele, visted)
                if ele not in visted:
                    q.extend(ele)
                visted.add(top)
        return res