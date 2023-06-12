class FileSystem:

    def __init__(self):
        self.fs = defaultdict(set)
        self.files = defaultdict(str)

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split("/")[-1]]
        
        if path == "/":
            path = ""
            
        return sorted(self.fs[path])
    
    
    def mkdir(self, path: str) -> None:
        dirs = path.split("/")
        path = ""
        for d in dirs[1:]:
            self.fs[path].add(d)
            path += "/" + d
                    

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")
        
        d = "/".join(path[:-1])
        self.mkdir(d)
        
        file = path[-1]
        self.fs[d].add(file)
        self.files[filePath] += content
        

    def readContentFromFile(self, filePath: str) -> str:
        if filePath not in self.files:
            return ""
        
        return self.files[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
