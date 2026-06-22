class FileSystem:

    def __init__(self):
        self.paths = dict()
        

    def createPath(self, path: str, value: int) -> bool:
        
        if self.paths.get(path, -1) != -1:
            return False

        s = path[1:].split("/")
        
        if len(s) == 1:
            self.paths[path] = value
        else:
            parent = "/" + "/".join(s[:-1])
            if self.paths.get(parent, -1) == -1:
                return False
            self.paths[path] = value
        
        return True
        

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)