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


import re


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        targetHost = self.getHost(startUrl)
        
        seen = set()
        res = []
        
        def dfs(url: str) -> None:
            if url in seen:
                return
            seen.add(url)          
            if targetHost == self.getHost(url):
                res.append(url)
                for nextUrl in htmlParser.getUrls(url):
                    dfs(nextUrl)          
        
        dfs(startUrl)
        return res
        
    
    def getHost(self, url: str) -> str:
        match = re.search(r"^http://([^/]+)", url)
        return match.groups()[0]
