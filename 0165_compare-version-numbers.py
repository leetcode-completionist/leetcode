class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        versions_1 = version1.split(".")
        versions_2 = version2.split(".")
        
        while len(versions_1) < len(versions_2):
            versions_1.append("0")
        
        while len(versions_2) < len(versions_1):
            versions_2.append("0")
            
        for v1, v2 in zip(versions_1, versions_2):
            v1 = int(v1)
            v2 = int(v2)
            if v1 == v2:
                continue
                
            if v1 < v2:
                return -1
            else:
                return 1
            
        return 0
