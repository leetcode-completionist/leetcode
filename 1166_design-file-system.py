class FileSystem:

    def __init__(self):
        self.file_system = {}

    def createPath(self, path: str, value: int) -> bool:
        if path == "" or path == "/" or path in self.file_system:
            return False
        
        key = ""
        directories = path.split("/")
        for directory in directories[1:-1]:
            key += "/" + directory
            if key not in self.file_system:
                return False
        
        self.file_system[key + "/" + directories[-1]] = value
        return True
        

    def get(self, path: str) -> int:
        if path not in self.file_system:
            return -1
        return self.file_system[path]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
